from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("", views.Account.as_view(), name="account"),
    path("login/", views.Login.as_view(), name="login"),
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", views.Logout.as_view(), name="logout")
] 
