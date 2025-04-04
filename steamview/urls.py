from django.urls import path
from steamview.views import paginaJogo, searchBar, api_jogos, ratingSearchPage

urlpatterns = [
    path("", paginaJogo, name = "paginaJogo"),
    path("search/", searchBar, name ="searchBar"),
    path("ratingsearch/api/", api_jogos, name="api_jogos"),
    path("ratingsearch/", ratingSearchPage, name="ratingSearchPage")
]