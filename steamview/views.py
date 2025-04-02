from django.shortcuts import render
import requests

def paginaJogo(request):
    game_name = "dark souls"

    url_all_games = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url_all_games)

    if response.status_code == 200:
        games = response.json()["applist"]["apps"]
    else:
        games = None

    appId = None
    if games:
        for game in games:
            if game_name.lower() in game["name"].lower():
                appId = game["appid"]
                break

    gameInfo = None
    if appId:
        url_game_details = f"https://store.steampowered.com/api/appdetails?appids={appId}"
        response = requests.get(url_game_details)

        if response.status_code == 200:
            data = response.json()
            if data[str(appId)]["success"]:
                game_details = data[str(appId)]["data"]

                gameInfo = {
                    "name": game_details.get("name", "N/A"),
                    "description": game_details.get("short_description", "Descrição não disponível."),
                    "price": game_details.get("price_overview", {}).get("final_formatted", "Preço não disponível"),
                    "image_url": game_details.get("header_image", "Imagem não disponível")
                }

    context = {
        "gameInfo": gameInfo
    }

    return render(request, "paginaJogo.html", context)
