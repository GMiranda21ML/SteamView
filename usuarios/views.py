from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("paginaJogo")
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, "usuarios/login.html")

def cadastro(request):    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "As senhas não coincidem")
        elif User.objects.filter(username = username).exists():
            messages.error(request, "Nome de usuário já existe")
        elif User.objects.filter(email = email).exists():
            messages.error(request, "E-mail já cadastrado")
        else:
            user = User.objects.create_user(
                username = username, 
                email = email, 
                password = password1
            )
            user.save()
            messages.success(request, "Cadastro reealizado com sucesso!")
            return redirect("login") 
           
    return render(request, "usuarios/cadastro.html")