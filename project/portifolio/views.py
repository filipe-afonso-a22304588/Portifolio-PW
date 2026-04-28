##  ficheiro escola/views.py

from django.shortcuts import render
from .models import Docente,Competencia,Empresa,Formacao,TFC,Tecnologia,UC,Projeto,Licenciatura,MakingOF

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