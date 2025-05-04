from django.urls import path, re_path
from steamview.views import paginaJogo, searchBar, api_jogos, ratingSearchPage,lancamentos_recentes, maisJogados, maisJogadosHist, configHardware, jogoAleatorio
urlpatterns = [
    path("", searchBar, name ="searchBar"),
    path("ratingsearch/api/", api_jogos, name="api_jogos"),
    path("ratingsearch/", ratingSearchPage, name="ratingSearchPage"),
    re_path(r'^jogo/(?P<nome>.+)/$', paginaJogo, name='paginaJogo'),
    path("lancamentos/", lancamentos_recentes, name="lancamentos_recentes"),
    path("maisjogados/", maisJogados, name="maisJogados"),
    path("maisJogadosHist/", maisJogadosHist, name="maisJogadosHist"),
    path("configHardware/",configHardware, name = "configHardware"),
    path("jogoAleatorio/", jogoAleatorio, name = "jogoAleatorio"),
]