from django.urls import path, re_path
from steamview.views import paginaJogo, searchBar, api_jogos, ratingSearchPage,lancamentos_recentes, maisJogados, maisJogadosHist, \
    jogoAleatorio, wishList, adicionarWishlist, removerWishlist

urlpatterns = [
    path("", searchBar, name ="searchBar"),
    path("ratingsearch/api/", api_jogos, name="api_jogos"),
    path("ratingsearch/", ratingSearchPage, name="ratingSearchPage"),
    re_path(r'^jogo/(?P<nome>.+)/$', paginaJogo, name='paginaJogo'),
    path("lancamentos/", lancamentos_recentes, name="lancamentos_recentes"),
    path("maisjogados/", maisJogados, name="maisJogados"),
    path("maisJogadosHist/", maisJogadosHist, name="maisJogadosHist"),
    path("jogoAleatorio/", jogoAleatorio, name = "jogoAleatorio"),
    path("wishList/", wishList, name= "wishList"),
    path("wishlist/adicionar/", adicionarWishlist, name="adicionarWishlist"),
    path("wishlist/remover/", removerWishlist, name="removerWishlist"),

]