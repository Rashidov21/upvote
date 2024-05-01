from django.urls import path
from django.contrib.auth import views as auth_views

from . import views  


app_name = "vote"

urlpatterns = [
    # AUTH 
    path("login/", auth_views.LoginView.as_view(
        template_name="auth/login.html"), name="login")
]
