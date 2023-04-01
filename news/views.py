from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Link, Comment
from .mixins import LinkAccessMixin, CommentAccessMixin
from account.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

class Home(ListView):
    model = Link
    template_name = "news/home.html"


class LinkCreate(LoginRequiredMixin, CreateView):
    model = Link
    fields = ("title", "url", "description")
    success_url = reverse_lazy('account:account')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super(LinkCreate, self).form_valid(form)


class CommentCreate(CreateView):
    model = Comment
    fields = ("text",)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.pk = self.kwargs.get("pk")
        self.object.link = Link.objects.get(id=self.kwargs.get("pk"))
        return super(CommentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["link"] = get_object_or_404(Link, id=self.kwargs.get("pk"))
        return context

    def get_success_url(self):
        return reverse_lazy('news:comment-create', args=(self.kwargs.get("pk"),))


class LinkDelete(LoginRequiredMixin, LinkAccessMixin, DeleteView):
    model = Link
    success_url = reverse_lazy("account:account")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["link"] = get_object_or_404(Link, id=self.kwargs.get("pk"))
        return context


class CommentDelete(LoginRequiredMixin, CommentAccessMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('news:comment-create', args=(self.kwargs.get("pk"),))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment"] = get_object_or_404(Comment, id=self.kwargs.get("com_pk"))
        context["link"] = get_object_or_404(Link, id=self.kwargs.get("pk"))
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Comment, id=self.kwargs.get("com_pk"))


@login_required(login_url="account:login")
def like(request, pk):
    user = get_object_or_404(User, id=request.user.id)
    link = get_object_or_404(Link, id=pk)
    if user in link.dislike.all():
        link.dislike.remove(user)
        link.like.add(user)
    elif user in link.like.all():
        link.like.remove(user)
    else:
        link.like.add(user)
    return redirect("news:comment-create", pk=pk)


@login_required(login_url="account:login")
def dislike(request, pk):
    user = get_object_or_404(User, id=request.user.id)
    link = get_object_or_404(Link, id=pk)
    if user in link.like.all():
        link.like.remove(user)
        link.dislike.add(user)
    elif user in link.dislike.all():
        link.dislike.remove(user)
    else:
        link.dislike.add(user)
    return redirect("news:comment-create", pk=pk)


def link(request, pk):
    link = get_object_or_404(Link, id=pk)

    return JsonResponse({
        "like": link.like.count(),
        "dislike": link.dislike.count(),
        "status": request.user.is_authenticated
    })
