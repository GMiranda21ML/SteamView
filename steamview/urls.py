from django.urls import path
from steamview.views import paginaJogo

urlpatterns = [
    path("", paginaJogo, name = "paginaJogo"),
]