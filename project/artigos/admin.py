from django.contrib import admin
from .models import Artigo
from django.utils.html import format_html

class ArtigoAdmin(admin.ModelAdmin):

    list_display = ('texto', 'fotografia', 'link_clicavel', 'data_criacao', 'autor')
    ordering = ('texto',)
    search_fields = ('texto', 'autor__username',)
    
    def link_clicavel(self, obj):
        if not obj.link or not obj.link.strip():
            return "Não associado"
        return format_html('<a href="{}" target="_blank">Abrir</a>', obj.link)
    
    link_clicavel.short_description = "Link"

admin.site.register(Artigo,ArtigoAdmin)

