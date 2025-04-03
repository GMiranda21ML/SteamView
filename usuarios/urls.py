from django.urls import path
from usuarios.views import cadastro

urlpatterns = [
    path("cadastro/", cadastro, name = "cadastro"),
]