##  ficheiro escola/views.py

from django.shortcuts import render
from .models import Curso,Professor,Aluno

def cursos_view(request):

    cursos = Curso.objects.select_related('professor').prefetch_related('alunos').all()
    
    return render(request, 'escola/curso.html', {'cursos': cursos})

def professores_view(request):

    professores = Professor.objects.all()
    
    return render(request, 'escola/professor.html', {'professores': professores})