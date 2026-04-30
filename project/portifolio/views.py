##  ficheiro escola/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente,Competencia,Empresa,Formacao,TFC,Tecnologia,UC,Projeto,Licenciatura,MakingOF
from .forms import ProjetoForm

def ucs_view(request):

    ucs = UC.objects.all()
    
    return render(request, 'portifolio/ucs.html', {'ucs': ucs})

def uc_view(request, id):
    uc = UC.objects.get(id=id)
    return render(request, 'portifolio/uc.html', {'uc': uc})


def projetos_view(request):

    projetos = Projeto.objects.all()
    
    return render(request, 'portifolio/projetos.html', {'projetos': projetos})

def projeto_view(request, id):
    projeto=Projeto.objects.get(id=id)       
    return render(request, 'portifolio/projeto.html', {'projeto': projeto})

def licenciaturas_view(request):

    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portifolio/licenciaturas.html', {'licenciaturas': licenciaturas})

def licenciatura_view(request, id):
    licenciatura=Licenciatura.objects.get(id=id)       
    return render(request, 'portifolio/licenciatura.html', {'licenciatura': licenciatura})

def docente_view(request, id):
    docente = Docente.objects.get(id=id)
    return render(request, 'portifolio/docente.html', {'docente': docente})

def empresas_view(request):

    empresas = Empresa.objects.all()
    return render(request, 'portifolio/empresas.html', {'empresas': empresas})

def tfcs_view(request):

    tfcs = TFC.objects.all()
    return render(request, 'portifolio/tfcs.html', {'tfcs': tfcs})

def novo_projeto_view(request):

     # criar instância de formulário.
    # Se foram submetidos dados, estes estão em request.POST e o formulario com dados é válido. 
    # Senão, o form não tem dados e não é válido
    form = ProjetoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('projetos')
    
    context = {'form': form}
    return render(request, 'portifolio/novo_projeto.html', context)