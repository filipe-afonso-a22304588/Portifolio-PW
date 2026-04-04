from django.contrib import admin
from django.utils.html import format_html
from .models import Docente, Competencia, Empresa, Formacao, TFC, Tecnologia

admin.site.register(Docente)
admin.site.register(Competencia)
admin.site.register(Empresa)
admin.site.register(Formacao)
admin.site.register(TFC)
admin.site.register(Tecnologia)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'link_clicavel')

    def link_clicavel(self, obj):
        return format_html('<a href="{}" target="_blank">Abrir</a>', obj.link)