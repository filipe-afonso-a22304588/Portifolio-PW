#
import json
from django.core.management.base import BaseCommand
from portifolio.models import Docente, TFC, Tecnologia

class Command(BaseCommand):
    help = 'Importar TFCs do JSON'

    def handle(self, *args, **kwargs):
        TFC.objects.all().delete()
        with open('media/jsons/tfcs.json', encoding='utf-8') as tfc:
            dados = json.load(tfc)

        for item in dados:
            try:

                tecnologias = item.get('tecnologias') or ''
                lista_tecnologias = [tecnologia.strip() for tecnologia in tecnologias.split(';')]
                tecnologias_objs = []

                for nome_tecnologia in lista_tecnologias:
                    tecnologia, created = Tecnologia.objects.get_or_create(nome=nome_tecnologia)
                    tecnologias_objs.append(tecnologia)

                if item['tecnologias'] is None:
                    tecnologias_usadas_tfc = "-"
                else:
                    tecnologias_usadas_tfc=item['tecnologias'],


                tfc_formatado = TFC.objects.create(
                    titulo=item['titulo'],
                    autor=item['autor'],
                    resumo=item['resumo'],
                    tecnologias_usadas=tecnologias_usadas_tfc,
                    docente_responsavel=item['orientador'],
                    interesse=5.0  # ou outro valor default
                )

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro no TFC: {item.get('titulo')} -> {e}"))
#