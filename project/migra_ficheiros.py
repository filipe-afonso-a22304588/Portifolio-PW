import os
from django.core.files import File
from escola.models import Curso 
from portfolio.models import Tecnologia,Projeto,MakingOF  # adaptar ao modelo

for obj in Curso.objects.all():
    if obj.imagem and obj.imagem.name:   # adaptar o nome do campo (neste caso é "imagem")
        local_path = obj.imagem.path    # adequar

        if os.path.exists(local_path):
            print(obj.nome)

            with open(local_path, 'rb') as f:
                obj.imagem.save(                         # adequar
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")

for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:   # adaptar o nome do campo (neste caso é "imagem")
        local_path = obj.logo.path    # adequar

        if os.path.exists(local_path):
            print(obj.nome)
            with open(local_path, 'rb') as f:
                obj.logo.save(                         # adequar
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")

for obj in Projeto.objects.all():
    if obj.exemplo and obj.exemplo.name:   # adaptar o nome do campo (neste caso é "imagem")
        local_path = obj.exemplo.path    # adequar

        if os.path.exists(local_path):
            print(obj.titulo)
            with open(local_path, 'rb') as f:
                obj.exemplo.save(                         # adequar
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")
        else:
            print("erro")

for obj in MakingOF.objects.all():
    if obj.imagem and obj.imagem.name:   # adaptar o nome do campo (neste caso é "imagem")
        local_path = obj.imagem.path    # adequar

        if os.path.exists(local_path):
            print(obj.titulo)

            with open(local_path, 'rb') as f:
                obj.imagem.save(                         # adequar
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")

"""for obj in Curso.objects.all():
    if obj.imagem and obj.imagem.name:
        try:
            with obj.imagem.open('rb') as f:
                obj.imagem.save(
                    obj.imagem.name,
                    File(f),
                    save=True
                )
        except Exception as e:
            print(f"Erro em Curso {obj}: {e}")

for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        try:
            with obj.logo.open('rb') as f:
                obj.logo.save(
                    obj.logo.name,
                    File(f),
                    save=True
                )
        except Exception as e:
            print(f"Erro em Curso {obj}: {e}")

for obj in Projeto.objects.all():
     if obj.exemplo and obj.exemplo.name:
        try:
            with obj.exemplo.open('rb') as f:
                obj.exemplo.save(
                    obj.exemplo.name,
                    File(f),
                    save=True
                )
        except Exception as e:
            print(f"Erro em Curso {obj}: {e}")

for obj in MakingOF.objects.all():
     if obj.imagem and obj.imagem.name:
        try:
            with obj.imagem.open('rb') as f:
                obj.imagem.save(
                    obj.imagem.name,
                    File(f),
                    save=True
                )
        except Exception as e:
            print(f"Erro em Curso {obj}: {e}")"""