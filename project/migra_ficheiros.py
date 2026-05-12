import os

from django.conf import settings
from django.core.files import File

from escola.models import Curso
from portfolio.models import Tecnologia, Projeto, MakingOF


def migrar_imagem(obj, campo, nome_objeto="Objeto"):

    ficheiro = getattr(obj, campo)

    if not ficheiro or not ficheiro.name:
        print(f"{nome_objeto} sem ficheiro")
        return

    local_path = os.path.join(
        settings.MEDIA_ROOT,
        ficheiro.name
    )

    if not os.path.exists(local_path):
        print(f"Ficheiro não encontrado: {local_path}")
        return

    try:

        with open(local_path, 'rb') as f:

            ficheiro.save(
                os.path.basename(local_path),
                File(f),
                save=True
            )

        print(f"Migrado: {obj}")

    except Exception as e:
        print(f"Erro em {obj}: {e}")


# CURSOS
for obj in Curso.objects.all():

    print(f"\nCurso: {obj.nome}")

    migrar_imagem(
        obj,
        'imagem',
        'Curso'
    )


# TECNOLOGIAS
for obj in Tecnologia.objects.all():

    print(f"\nTecnologia: {obj.nome}")

    migrar_imagem(
        obj,
        'logo',
        'Tecnologia'
    )


# PROJETOS
for obj in Projeto.objects.all():

    print(f"\nProjeto: {obj.titulo}")

    migrar_imagem(
        obj,
        'exemplo',
        'Projeto'
    )


# MAKING OF
for obj in MakingOF.objects.all():

    print(f"\nMakingOF: {obj.titulo}")

    migrar_imagem(
        obj,
        'imagem',
        'MakingOF'
    )


print("\nMigração concluída.")