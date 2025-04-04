from django.urls import path
from steamview.views import paginaJogo, searchBar, api_jogos, ratingSearchPage

urlpatterns = [
    path("", searchBar, name ="searchBar"),
    path("ratingsearch/api/", api_jogos, name="api_jogos"),
    path("ratingsearch/", ratingSearchPage, name="ratingSearchPage"),
    path("jogo/<str:nome>/", paginaJogo, name="paginaJogo"),

]