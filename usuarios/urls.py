from django.urls import path
from usuarios.views import loginView, cadastro

urlpatterns = [
    path("login/", loginView, name = "login"),
    path("cadastro/", cadastro, name = "cadastro"),
]