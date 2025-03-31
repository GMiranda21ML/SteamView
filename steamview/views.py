from django.shortcuts import render

# Create your views here.

def paginaJogo(request):
    return render(request, "paginaJogo.html")