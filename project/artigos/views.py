from django.shortcuts import render
from .models import Artigo
from .forms import RegistoForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

def artigos_view(request):

    artigos = Artigo.objects.all()
    is_autor = request.user.groups.filter(name='autores').exists()

    
    return render(request, 'artigos/artigos.html', {'artigos': artigos, 'is_autor': is_autor})


def artigo_view(request, id):
    artigo = Artigo.objects.get(id=id)
    is_gestor = request.user.groups.filter(name='gestor-portifolio').exists()

    return render(request, 'artigos/artigo.html', {'artigo': artigo, 'is_gestor': is_gestor})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('artigos')
        else:
            return render(request, 'artigos/login.html', {'erro: Credenciais inválidas'})

    return render(request, 'artigos/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    
def registo_view(request):

    if request.method == "POST":
        form = RegistoForm(request.POST)

        if form.is_valid():

            user = form.save()

            grupo_autores = Group.objects.get(name="autores")

            user.groups.add(grupo_autores)

            return redirect('login')

    else:
        form = RegistoForm()

    context = {
        'form': form
    }

    return render(request, 'artigos/registo.html', context)

def account_view(request):
    return render(request, 'artigos/account.html')

def logout_view(request):
    logout(request)
    return redirect('conta')


