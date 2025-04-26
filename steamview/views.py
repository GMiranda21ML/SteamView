from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_page
from django.contrib.auth.models import User
from django.contrib import messages
from bs4 import BeautifulSoup
from .models import Jogos, HistoricoPesquisa, MaisJogados
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.core.cache import cache
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

def importar_jogos():
    nomes = [
        "Hollow Knight",
        "Stardew Valley",
        "Celeste",
        "The Witcher 3: Wild Hunt",
        "Red Dead Redemption 2",
        "Portal 2",
        "Terraria",
        "Hades",
        "Undertale",
        "Bioshock Infinite",
        "Cuphead",
        "It Takes Two",
        "Don't Starve",
        "Dark Souls III",
        "Sekiro: Shadows Die Twice",
        "Slay the Spire",
        "Subnautica",
        "Dead Cells",
        "Outer Wilds",
        "Hogwarts Legacy"
    ]

    for nome in nomes:
        if Jogos.objects.filter(name__iexact=nome).exists():
            print(f"{nome} já está no banco.")
            continue

        game = buscarJogoPorNome(nome)
        if game:
            game_id = game.get("id")
            detalhes = buscarDetalhesDoJogo(game_id)
            preco = buscarPrecoSteam(nome)

            if detalhes:
                descricao_html = detalhes.get("description", "Descrição não disponível.")
                descricao_limpa = BeautifulSoup(descricao_html, "html.parser").get_text()

                novo_jogo = Jogos(
                    name = detalhes.get("name", "N/A"),
                    description = descricao_limpa,
                    rating = detalhes.get("rating", "0.0"),
                    image = detalhes.get("background_image", ""),
                    price = preco
                )
                novo_jogo.save()
                print(f"✅ {nome} importado com sucesso.")
            else:
                print(f"❌ Detalhes não encontrados para {nome}")
        else:
            print(f"❌ Jogo não encontrado: {nome}")

# view da paginaJogo
@csrf_exempt
def paginaJogo(request, nome):

    if not request.user.is_authenticated:
        return redirect("login")

    game_name = nome
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
        "gameInfo": gameInfo,
        "nome": nome,
    }

    return render(request, "steamview/paginaJogo.html", context)

def remover_duplicatas():
    nomes_vistos = set()
    jogos = Jogos.objects.all().order_by('id')  # manter o primeiro inserido

    for jogo in jogos:
        nome_normalizado = jogo.name.strip().lower()
        if nome_normalizado in nomes_vistos:
            print(f"Removendo duplicata: {jogo.name}")
            jogo.delete()
        else:
            nomes_vistos.add(nome_normalizado)

    print("Limpeza de duplicatas finalizada!")

def api_jogos(request):
    page_number = int(request.GET.get("page", 1))
    all_games = Jogos.objects.all().order_by('-rating')

    paginator = Paginator(all_games, 10)  # 6 por página
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        return JsonResponse({
            "games": [],
            "has_next": False
        })

    games_list = [
        {
            "name": jogo.name,
            "image": jogo.image,
            "price": jogo.price,
            "rating": jogo.rating
        }
        for jogo in page.object_list
    ]

    return JsonResponse({
        "games": games_list,
        "has_next": page.has_next()
    })

def ratingSearchPage(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "steamview/ratingsearch.html")


def searchBar(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.method == "GET":
        nome = request.GET.get("nome")
        
        if nome: 
            historico = HistoricoPesquisa.objects.filter(name=nome).first()
            
            if historico:  
                historico.frequency += 1  
                historico.save()  
            else:
                historico = HistoricoPesquisa(
                    name=nome,
                    frequency=1
                )
                historico.save()  
            
            return redirect("paginaJogo", nome=nome)

    return render(request, "steamview/searchbar.html")


def lancamentos(request):
    return render(request, 'steamview/lancamentos.html')


def maisJogados(request):
    if not request.user.is_authenticated:
        return redirect("login")

    jogos = []

    data = cache.get('mais_jogados_data')

    if not data:
        url = "https://api.steampowered.com/ISteamChartsService/GetMostPlayedGames/v1/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            cache.set('mais_jogados_data', data, 60 * 15)  # 15 minutos de cache

    if data:
        games = data.get("response", {}).get("ranks", [])[:20]

        for game in games:
            appid = game.get("appid")
            current_players = 0

            details_url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
            details_response = requests.get(details_url)

            nome = "Nome não disponível"
            imagem = ""

            if details_response.status_code == 200:
                details_data = details_response.json().get(str(appid), {}).get("data", {})
                nome = details_data.get("name", "Nome não disponível")
                imagem = details_data.get("header_image", "")

            players_url = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={appid}"
            players_response = requests.get(players_url)

            if players_response.status_code == 200:
                players_data = players_response.json()
                current_players = players_data.get("response", {}).get("player_count", 0)

            if not MaisJogados.objects.filter(name=nome).exists():
                MaisJogados.objects.create(
                    name=nome,
                    players=current_players,
                    image=imagem
                )

            jogos.append({
                "nome": nome,
                "imagem": imagem,
                "current_players": current_players
            })

    context = {
        "jogos": jogos
    }
    return render(request, "steamview/maisjogados.html", context)