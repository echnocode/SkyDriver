from django.urls import path

from .views import sign_in, sign_out, sign_up

urlpatterns = [
    path("register/", sign_up, name="register"),
    path("login/", sign_in, name="login"),
    path("logout/", sign_out, name="logout"),
]
