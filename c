{% extends "shared/base.html" %}
{% load socialaccount %}
{% load static %}

{% block content %}
<main class="login">
    <div class="search-wrapper" style="
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 40px;
        background-color: rgba(27, 40, 56, 0.85);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(102, 192, 244, 0.3);
        border-radius: 15px;
        box-shadow: 0 4px 25px rgba(102, 192, 244, 0.25);
        width: 800px;
        margin: 80px auto;
        flex-direction: column;
    ">
        <h1 style="
            margin-bottom: 30px;
            font-size: 32px;
            text-align: center;
            font-family: 'Bungee', cursive;
            color: #ffffff;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
        ">SEARCH FOR ANY GAME</h1>
        
        <form method="GET" action="{% url 'search_results' %}" style="width: 100%;">
            <div class="search-container" style="
                display: flex;
                align-items: center;
                background-color: rgba(0, 0, 0, 0.3);
                border: 2px solid rgba(102, 192, 244, 0.4);
                border-radius: 10px;
                padding: 5px 15px;
                width: 100%;
                position: relative;
                transition: all 0.3s ease;
            ">
                <input type="text" 
                    name="query" 
                    placeholder="Search your game..." 
                    required 
                    style="
                        background: transparent;
                        color: white;
                        border: none;
                        outline: none;
                        font-size: 18px;
                        width: 100%;
                        font-family: 'Roboto', sans-serif;
                        height: 45px;
                        padding: 0 10px;
                    "
                >
                <button class="search-button" 
                    type="submit" 
                    style="
                        background: transparent;
                        border: none;
                        cursor: pointer;
                        padding: 8px;
                        position: absolute;
                        right: 10px;
                        transition: transform 0.2s ease;
                    "
                >
                    <img src="{% static 'img/search.png' %}" 
                        alt="Search" 
                        style="
                            width: 24px; 
                            height: 24px;
                            opacity: 0.8;
                            transition: opacity 0.2s ease;
                        "
                    >
                </button>
            </div>
        </form>
    </div>
</main>
{% endblock %}