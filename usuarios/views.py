from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def cadastro(request):        
    return render(request, "usuarios/cadastro.html")