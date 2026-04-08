import requests, json, os
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Importar dados da API'

    def handle(self, *args, **kwargs):
        print("OK")

    schoolYear = '202526'
    course = 260  # LEI

    for language in ['PT', 'ENG']:

        url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'

        payload = {
            'language': language,
            'courseCode': course,
            'schoolYear': schoolYear
        }
    
        # Set the content-type header to 'application/json'
        headers = {'content-type': 'application/json'}

        # Send the POST request
        response = requests.post(url, json=payload, headers=headers)
        response_dict = response.json()

        # 📁 caminho correto
        pasta_cursos = os.path.join(settings.MEDIA_ROOT, 'jsons', 'Cursos')
        pasta_ucs = os.path.join(settings.MEDIA_ROOT, 'jsons', 'UCs')

        # garante que existem
        os.makedirs(pasta_cursos, exist_ok=True)
        os.makedirs(pasta_ucs, exist_ok=True)

        # 💾 guardar curso
        with open(os.path.join(pasta_cursos, f"ULHT{course}-{language}.json"), "w", encoding="utf-8") as f:
            json.dump(response_dict, f, indent=4)

        # 🔁 UCs
        for uc in response_dict['courseFlatPlan']:

            url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'

            # Define the payload data to be sent in the POST request
            payload = {
                'language': language,
                'curricularIUnitReadableCode': uc['curricularIUnitReadableCode'],
            }

            # Send the POST request
            response_uc = requests.post(url, json=payload, headers=headers)
            response_uc_dict = response_uc.json()

            with open(os.path.join(pasta_ucs, f"{uc['curricularIUnitReadableCode']}-{language}.json"), "w", encoding="utf-8") as f:
                json.dump(response_uc_dict, f, indent=4)