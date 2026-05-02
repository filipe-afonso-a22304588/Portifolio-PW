import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from portifolio.models import UC

class Command(BaseCommand):
    help = 'Importar UCs dos JSONs'

    def handle(self, *args, **kwargs):

        pasta_ucs = os.path.join(settings.MEDIA_ROOT, 'jsons', 'UCs')

        for ficheiro in os.listdir(pasta_ucs):

            if not ficheiro.endswith('.json'):
                continue

            caminho = os.path.join(pasta_ucs, ficheiro)

            with open(caminho, encoding='utf-8') as f:
                data = json.load(f)

            nome = data.get('curricularUnitName')
            resumo = (data.get('presentation') or '')[:100]  # ⚠️ corta para caber no CharField
            ect = data.get('ects')
            ano = data.get('curricularYear')

            #Semestre não vem direto
            semestre = 1 if "1" in ficheiro else 2

            uc, created = UC.objects.get_or_create(
                nome=nome,
                defaults={
                    'resumo': resumo,
                    'ect': ect,
                    'ano_curricular': ano,
                    'semestre': semestre
                }
            )

        self.stdout.write(self.style.SUCCESS('UCs importadas!'))