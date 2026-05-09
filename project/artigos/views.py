from django.shortcuts import render
from .models import Artigo
from .forms import RegistoForm, ArtigoForm, ComentarioForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

def artigos_view(request):

    artigos = Artigo.objects.all()
    is_gestor = request.user.groups.filter(name='autores').exists()
    
    return render(request, 'artigos/artigos.html', {'artigos': artigos, 'is_gestor': is_gestor})

def artigo_view(request, id):
    artigo = Artigo.objects.get(id=id)
    is_gestor = request.user.groups.filter(name='autores').exists()
    is_autor = request.user == artigo.autor

    return render(request, 'artigos/artigo.html', {'artigo': artigo, 'is_gestor': is_gestor, 'is_autor':is_autor})

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

def edita_artigo_view(request, artigo_id):

    artigo = Artigo.objects.get(id=artigo_id)
    
    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigo', id=artigo_id)
    else:
        form = ArtigoForm(instance=artigo)
        
    context = {'form': form, 'artigo':artigo}
    return render(request, 'artigos/editar_artigo.html', context)

def apaga_artigo_view(request, artigo_id):

    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('artigos')

def novo_artigo_view(request):
    
    form = ArtigoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('artigos')
    
    context = {'form': form}
    return render(request, 'artigos/novo_artigo.html', context)

@login_required
def like_artigo(request, id):

    artigo = Artigo.objects.get(id=id)

    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)

    return redirect('artigo', id=id)

@login_required
def adicionar_comentario(request, id):

    artigo = Artigo.objects.get(id=id)

    if request.method == "POST":

        form = ComentarioForm(request.POST)

        if form.is_valid():

            comentario = form.save(commit=False)

            comentario.artigo = artigo
            comentario.autor = request.user

            comentario.save()

    return redirect('artigo', id=id)