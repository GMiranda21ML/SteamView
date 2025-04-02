from django.shortcuts import render
from bs4 import BeautifulSoup  
import requests

API_KEY = "2965d09ddf6e4c47ad963c0a15e4e7db"  

# Buscando o jogo pelo nome usando a API da RAWG e retorna seu ID.
def buscar_jogo_por_nome(game_name):
    url = f"https://api.rawg.io/api/games?key={API_KEY}&search={game_name}"
    response = requests.get(url)

    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]  
    return None


