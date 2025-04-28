from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_page
from django.contrib.auth.models import User
from django.contrib import messages
from bs4 import BeautifulSoup
from .models import Jogos, HistoricoPesquisa, MaisJogados, MaisJogadosHist, MenosJogadosHist
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.core.cache import cache
from datetime import datetime, timedelta
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

@csrf_exempt
def lancamentos_recentes(request):
    if not request.user.is_authenticated:
        return redirect("login")

    jogos_query = Jogos.objects.filter(released_date__isnull=False).order_by('-released_date')[:100] # ver para mudar depois de 100 para 50, VOCE SABERÁ O PQ

    jogos = []
    for jogo in jogos_query:
        jogos.append({
            "nome": jogo.name,
            "imagem": jogo.image if jogo.image else 'https://via.placeholder.com/300x400?text=Sem+Imagem',
            "rating": jogo.rating,
            "preco": jogo.price,
            "lancamento": jogo.released_date
        })

    context = {
        "jogos": jogos
    }

    return render(request, 'steamview/lancamentos.html', context)

def importar_jogos_recentes():
    page = 1
    total_importados = 0
    data_inicio = "2024-01-01"
    data_fim = "2025-12-31"

    while True:
        url = f"https://api.rawg.io/api/games?dates={data_inicio},{data_fim}&ordering=-released&page_size=40&page={page}&key={API_KEY}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Erro na página {page}: {response.status_code}")
            break

        data = response.json()
        results = data.get('results', [])

        if not results:
            break

        for game in results:
            nome = game.get('name')
            released_date = game.get('released')
            imagem = game.get('background_image') or 'https://via.placeholder.com/300x400?text=Sem+Imagem'
            rating = game.get('rating', 0.0)

            if not nome or not released_date:
                continue

            if Jogos.objects.filter(name__iexact=nome).exists():
                print(f"🔵 {nome} já está no banco. Pulando...")
                continue

            descricao = game.get('description_raw') or "Descrição não disponível."

            novo_jogo = Jogos(
                name=nome,
                description=descricao,
                rating=rating,
                image=imagem,
                price="Preço não disponível",
                released_date=released_date
            )
            novo_jogo.save()
            total_importados += 1

            print(f"✅ {nome} importado.")

        page += 1

    print(f"Importação finalizada. Total de jogos importados: {total_importados}")

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
    order = request.GET.get('order', 'desc')

    if order == 'asc':
        all_games = Jogos.objects.all().order_by('rating')  # Menor para maior
    else:
        all_games = Jogos.objects.all().order_by('-rating')  # Maior para menor


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


def maisJogadosHist(request):
    data_inicio = '2015-01-01'
    data_fim = '2025-04-26'
    filtro = request.GET.get('filter', 'mais-jogados') 

    jogos = []
    page = 1

    if filtro == 'mais-jogados':
        ordering = '-added'
    elif filtro == 'menos-jogados':
        ordering = 'added'

    while len(jogos) < 100:
        url = f"https://api.rawg.io/api/games?dates={data_inicio},{data_fim}&ordering={ordering}&key={API_KEY}&page_size=20&page={page}"
        response = requests.get(url)
        data = response.json()

        for jogo in data.get('results', []):
            jogos.append({
                "nome": jogo.get('name'),
                "imagem": jogo.get('background_image'),
                "rating": jogo.get('rating'),
                "lancamento": jogo.get('released')
            })

            if filtro == "mais-jogados":
                if not MaisJogadosHist.objects.filter(name=jogo.get('name')).exists():
                    MaisJogadosHist.objects.create(
                        name=jogo.get('name'),
                        rating=jogo.get('rating'),
                        released=jogo.get('released'),
                        image=jogo.get('background_image'),
                    )
            elif filtro == "menos-jogados":
                if not MenosJogadosHist.objects.filter(name=jogo.get('name')).exists():
                    image_url = jogo.get('background_image')
                    if not image_url:
                        image_url = 'https://via.placeholder.com/150'

                    MenosJogadosHist.objects.create(
                        name=jogo.get('name'),
                        rating=jogo.get('rating'),
                        released=jogo.get('released'),
                        image=image_url,
                    )

        page += 1

        if len(data.get('results', [])) < 20:
            break

    jogos = jogos[:100]

    return render(request, 'steamview/maisJogadosHist.html', {"jogos": jogos, "filtro": filtro})        