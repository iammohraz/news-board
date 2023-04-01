from .models import Link, Comment
from django.http import HttpResponseNotFound


class LinkAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        link = Link.objects.get(id=kwargs.get("pk"))
        if request.user.id != link.user.id:
            return HttpResponseNotFound()
        return super().dispatch(request, *args, **kwargs)


class CommentAccessMixin:
    def dispatch(self, request, *args, **kwargs):
        comment = Comment.objects.get(id=kwargs.get("com_pk"))
        if request.user.id != comment.user.id:
            return HttpResponseNotFound()
        return super().dispatch(request, *args, **kwargs)
