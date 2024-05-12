from django.urls import path
from django.contrib.auth import views as auth_views

from . import views  


app_name = "vote"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    

    path("login/", auth_views.LoginView.as_view(
        template_name="auth/login.html"), name="login")
]
