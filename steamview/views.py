from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from bs4 import BeautifulSoup
from .models import Jogos
import requests

API_KEY = "2965d09ddf6e4c47ad963c0a15e4e7db"  

# Buscando o jogo pelo nome usando a API da RAWG e retorna seu ID.
def buscarJogoPorNome(game_name):
    url = f"https://api.rawg.io/api/games?key={API_KEY}&search={game_name}"
    response = requests.get(url)

    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]  
    return None


# Busca os detalhes completos do jogo usando o ID do jogo.
def buscarDetalhesDoJogo(game_id):
    url = f"https://api.rawg.io/api/games/{game_id}?key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()  
    return None

# Busca o preço do jogo na API da Steam (se disponível).
def buscarPrecoSteam(game_name):
    url_all_games = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url_all_games)
    
    if response.status_code == 200:
        games = response.json().get("applist", {}).get("apps", [])
        for game in games:
            if game_name.lower() in game["name"].lower():
                app_id = game["appid"]
                url_price = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
                response_price = requests.get(url_price)
                
                if response_price.status_code == 200:
                    data = response_price.json()
                    if data.get(str(app_id), {}).get("success", False):
                        return data[str(app_id)]["data"].get("price_overview", {}).get("final_formatted", "Preço não disponível")
    return "Preço não disponível"

# view da paginaJogo
@csrf_exempt
def paginaJogo(request):

    if not request.user.is_authenticated:
        return redirect("login")

    game_name = "elden ring"
    game = buscarJogoPorNome(game_name)

    gameInfo = None
    if game:
        game_id = game.get("id")
        game_details = buscarDetalhesDoJogo(game_id)
        preco = buscarPrecoSteam(game_name)

        if game_details:
            descricao_html = game_details.get("description", "Descrição não disponível.")
            descricao_limpa = BeautifulSoup(descricao_html, "html.parser").get_text()

            gameInfo = {
                "name": game_details.get("name", "N/A"),
                "description": descricao_limpa,
                "rating": game_details.get("rating", "Nota não disponível"),
                "image_url": game_details.get("background_image", "Imagem não disponível"),
                "price": preco
            }


            if not Jogos.objects.filter(name = game_details.get("name", "N/A")).exists():
                jogosBanco = Jogos(
                    name = game_details.get("name", "N/A"),
                    description = descricao_limpa,
                    rating = game_details.get("rating", "Nota não disponível"),
                    image = game_details.get("background_image", "Imagem não disponível"),
                    price =  preco
                )

                jogosBanco.save()

    context = {
        "gameInfo": gameInfo
    }

    return render(request, "steamview/paginaJogo.html", context)


def searchBar(request):
    return render(request, "steamview/searchbar.html")