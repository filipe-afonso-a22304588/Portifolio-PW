from django.contrib import admin
from django.utils.html import format_html
from .models import Docente

admin.site.register(Docente)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'link_clicavel')

    def link_clicavel(self, obj):
        return format_html('<a href="{}" target="_blank">Abrir</a>', obj.link)