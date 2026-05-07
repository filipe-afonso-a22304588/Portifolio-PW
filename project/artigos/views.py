from django.shortcuts import render
from .models import Artigo
from .forms import RegistoForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def artigos_view(request):

    artigos = Artigo.objects.all()
    
    return render(request, 'artigos/artigos.html', {'artigos': artigos})

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
    form = RegistoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')
    context = {'form': form}

    return render(request, 'artigos/registo.html', context)

def account_view(request):
    return render(request, 'artigos/account.html')

def logout_view(request):
    logout(request)
    return redirect('conta')


