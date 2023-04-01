from django.views.generic import ListView, CreateView
from news.models import Link
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm
from .mixins import LoggedInRedirectMixin


# Create your views here.


class Account(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Link.objects.filter(user=self.request.user)

    template_name = "account/account.html"


class Login(LoggedInRedirectMixin, LoginView):
    template_name = "account/login.html"


class Register(LoggedInRedirectMixin, CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('account:login')


class Logout(LoginRequiredMixin, LogoutView):
    pass
