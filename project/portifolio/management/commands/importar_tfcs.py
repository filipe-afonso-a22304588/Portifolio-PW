#
import json
from django.core.management.base import BaseCommand
from portifolio.models import Docente, TFC, Tecnologia

class Command(BaseCommand):
    help = 'Importar TFCs do JSON'

    def handle(self, *args, **kwargs):
        with open('media/TFCS json/tfcs.json', encoding='utf-8') as tfc:
            dados = json.load(tfc)

        for tfc in dados:

            orientadores = tfc.get('orientador', '')
            lista_orientadores = [orientador.strip() for orientador in orientadores.split(',')]
            docentes_objs = []

            for nome_docente in lista_orientadores:
                docente, created = Docente.objects.get_or_create(nome=nome_docente)
                docentes_objs.append(docente)

            tecnologias = tfc.get('tecnologias', '')
            lista_tecnologias = [tecnologia.strip() for tecnologia in tecnologias.split(';')]
            tecnologias_objs = []

            for nome_tecnologia in lista_tecnologias:
                tecnologia, created = Tecnologia.objects.get_or_create(nome=nome_tecnologia)
                tecnologias_objs.append(tecnologia)

            tfc_formatado = TFC.objects.create(
                titulo=tfc['titulo'],
                autor=tfc['autor'],
                resumo=tfc['resumo'],
                tecnologias_usadas=tfc['tecnologias'],
                interesse=5.0  # ou outro valor default
            )

            tfc_formatado.docente_responsavel.set(docentes_objs)

        self.stdout.write(self.style.SUCCESS('Importação concluída!'))
#