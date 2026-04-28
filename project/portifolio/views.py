##  ficheiro escola/views.py

from django.shortcuts import render
from .models import Docente,Competencia,Empresa,Formacao,TFC,Tecnologia,UC,Projeto,Licenciatura,MakingOF

def uc_view(request):

    ucs = UC.objects.all()
    
    return render(request, 'portifolio/uc.html', {'ucs': ucs})