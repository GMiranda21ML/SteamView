from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

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