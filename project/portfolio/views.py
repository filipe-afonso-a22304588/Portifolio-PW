##  ficheiro escola/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente,Competencia,Empresa,Formacao,TFC,Tecnologia,UC,Projeto,Licenciatura,MakingOF
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm, RegistoForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def ucs_view(request):

    ucs = UC.objects.all()
    
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})

def uc_view(request, id):
    uc = UC.objects.get(id=id)
    return render(request, 'portfolio/uc.html', {'uc': uc})

def projetos_view(request):

    projetos = Projeto.objects.all()
    
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def projeto_view(request, id):
    projeto=Projeto.objects.get(id=id)       
    return render(request, 'portfolio/projeto.html', {'projeto': projeto})

def licenciaturas_view(request):

    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def licenciatura_view(request, id):
    licenciatura=Licenciatura.objects.get(id=id)       
    return render(request, 'portfolio/licenciatura.html', {'licenciatura': licenciatura})

def docente_view(request, id):
    docente = Docente.objects.get(id=id)
    return render(request, 'portfolio/docente.html', {'docente': docente})

def empresas_view(request):

    empresas = Empresa.objects.all()
    return render(request, 'portfolio/empresas.html', {'empresas': empresas})

def tfcs_view(request):

    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})

def novo_projeto_view(request):

     # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido. 
    # Senão, o form não tem dados e não é válido
    form = ProjetoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('projetos')
    
    context = {'form': form}
    return render(request, 'portfolio/novo_projeto.html', context)

def edita_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    
    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('projeto', id=projeto_id)
    else:
        form = ProjetoForm(instance=projeto)
        
    context = {'form': form, 'projeto':projeto}
    return render(request, 'portfolio/edita_projeto.html', context)

def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return redirect('projetos')

def tecnologias_view(request):

    tecnologias = Tecnologia.objects.all()
    
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def tecnologia_view(request, id):
    tecnologia = Tecnologia.objects.get(id=id)
    return render(request, 'portfolio/tecnologia.html', {'tecnologia': tecnologia})

def nova_tecnologia_view(request):
    
    form = TecnologiaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('projetos')
    
    context = {'form': form}
    return render(request, 'portfolio/nova_tecnologia.html', context)

def edita_tecnologia_view(request, tecnologia_id):

    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    
    if request.POST:
        form = TecnologiaForm(request.POST or None, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('tecnologia', id=tecnologia_id)
    else:
        form = TecnologiaForm(instance=tecnologia)
        
    context = {'form': form, 'tecnologia':tecnologia}
    return render(request, 'portfolio/editar_tecnologia.html', context)

def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = Tecnologia.objects.get(id=tecnologia_id)
    tecnologia.delete()
    return redirect('projetos')

def competencias_view(request):
    
    competencias = Competencia.objects.all()
    
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})

def competencia_view(request, id):
    competencia = Competencia.objects.get(id=id)
    return render(request, 'portfolio/competencia.html', {'competencia': competencia})

def edita_competencia_view(request, competencia_id):

    competencia = Competencia.objects.get(id=competencia_id)
    
    if request.POST:
        form = CompetenciaForm(request.POST or None, request.FILES, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('competencia', id=competencia_id)
    else:
        form = CompetenciaForm(instance=competencia)
        
    context = {'form': form, 'competencia':competencia}
    return render(request, 'portfolio/editar_competencia.html', context)

def apaga_competencia_view(request, competencia_id):
    competencia = Competencia.objects.get(id=competencia_id)
    competencia.delete()
    return redirect('competencias')

def nova_competencia_view(request):
    
    form = CompetenciaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('competencias')
    
    context = {'form': form}
    return render(request, 'portfolio/nova_competencia.html', context)

def formacoes_view(request):

    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})

def formacao_view(request, id):
    formacao = Formacao.objects.get(id=id)
    return render(request, 'portfolio/formacao.html', {'formacao': formacao})

def nova_formacao_view(request):
    
    form = FormacaoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('formacoes')
    
    context = {'form': form}
    return render(request, 'portfolio/nova_formacao.html', context)

def edita_formacao_view(request, formacao_id):

    formacao = Formacao.objects.get(id=formacao_id)
    
    if request.POST:
        form = FormacaoForm(request.POST or None, request.FILES, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacao', id=formacao_id)
    else:
        form = FormacaoForm(instance=formacao)
        
    context = {'form': form, 'formacao':formacao}
    return render(request, 'portfolio/editar_formacao.html', context)

def apaga_formacao_view(request, formacao_id):

    formacao = Formacao.objects.get(id=formacao_id)
    formacao.delete()
    return redirect('formacoes')

def info_view(request):

    makingofs = MakingOF.objects.all()
    
    return render(request, 'portfolio/info.html', {'makingofs': makingofs})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('ucs')
        else:
            return render(request, 'portfolio/login.html', {'erro: Credenciais inválidas'})

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    
def registo_view(request):
    form = RegistoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')
    context = {'form': form}

    return render(request, 'portfolio/registo.html', context)