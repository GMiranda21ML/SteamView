from django.urls import path
from usuarios.views import loginView, cadastro, logoutView

urlpatterns = [
    path("login/", loginView, name = "login"),
    path("cadastro/", cadastro, name = "cadastro"),
    path("logout/", logoutView, name = "logout"),
]