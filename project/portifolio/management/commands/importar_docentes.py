import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from portifolio.models import Docente


class Command(BaseCommand):
    help = 'Importar docentes do JSON'

    def handle(self, *args, **kwargs):

        caminho = os.path.join(
            settings.MEDIA_ROOT,
            'jsons',
            'Cursos',
            'ULHT260-PT.json'
        )

        with open(caminho, encoding='utf-8') as f:
            data = json.load(f)

        # ⚠️ ajusta isto conforme o JSON real
        docentes_json = data.get('teachers', [])

        for docente in docentes_json:
            nome = docente.get('academicName') or docente.get('fullName')
            email = docente.get('email', None)

            obj, created = Docente.objects.get_or_create(nome=nome)

            if email:
                obj.email = email
                obj.save()

        self.stdout.write(self.style.SUCCESS('Docentes importados!'))