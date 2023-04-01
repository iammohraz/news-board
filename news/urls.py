from django.urls import path, include
from . import views

app_name = "news"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("new/", views.LinkCreate.as_view(), name="link-create"),
    path("news/<int:pk>/", views.CommentCreate.as_view(), name="comment-create"),
    path("news/<int:pk>/delete/", views.LinkDelete.as_view(), name="link-delete"),
    path("news/<int:pk>/like/", views.like, name="link-like"),
    path("news/<int:pk>/dislike/", views.dislike, name="link-dislike"),
    path("news/<int:pk>/about/", views.link, name="link-about"),
    path("news/<int:pk>/comments/<int:com_pk>/delete/", views.CommentDelete.as_view(), name="comment-delete"),
]
