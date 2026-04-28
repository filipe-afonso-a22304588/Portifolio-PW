##  ficheiro escola/views.py

from django.shortcuts import render
from .models import Docente,Competencia,Empresa,Formacao,TFC,Tecnologia,UC,Projeto,Licenciatura,MakingOF

def ucs_view(request):

    ucs = UC.objects.all()
    
    return render(request, 'portifolio/ucs.html', {'ucs': ucs})


def projetos_view(request):

    projetos = Projeto.objects.all()
    
    return render(request, 'portifolio/projetos.html', {'projetos': projetos})

def projeto_view(request, id):
    projeto=Projeto.objects.get(id=id)       
    return render(request, 'portifolio/projeto.html', {'projeto': projeto})