from django.urls import path
from steamview.views import paginaJogo, searchBar

urlpatterns = [
    path("", paginaJogo, name = "paginaJogo"),
    path("search/", searchBar, name ="searchBar"),
]