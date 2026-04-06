from django.contrib import admin
from django.utils.html import format_html
from .models import Docente, Competencia, Empresa, Formacao, TFC, Tecnologia, Projeto,UC, Licenciatura, MakingOF

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'link_clicavel')
    search_fields = ('nome',)
    
    def link_clicavel(self, obj):
        if not obj.link or not obj.link.strip():
            return "Não associado"
        return format_html('<a href="{}" target="_blank">Abrir</a>', obj.link)
    
    link_clicavel.short_description = "Linkedin"

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_comeco', 'data_saida', 'listar_competencias')
    search_fields = ('nome',)

    def listar_competencias(self, obj):
        return ", ".join([c.titulo for c in obj.competencias.all()])
    
    listar_competencias.short_description = "Competências"
    
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')
    search_fields = ('titulo',)

class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'listar_docente', 'interesse')
    search_fields = ('titulo', 'autor',)

    
    def listar_docente(self, obj):
        return ", ".join([docente.nome for docente in obj.docente_responsavel.all()])
   
    listar_docente.short_description = "Docentes"

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mostrar_logo', 'listar_docente')
    search_fields = ('nome','docente__nome')

    def mostrar_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "-"
    
    mostrar_logo.short_description = "Logo"
    
    def listar_docente(self, obj):
        return ", ".join([docente.nome for docente in obj.docente.all()])

    listar_docente.short_description = "Docentes"

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'listar_docente', 'nota_final', 'link_clicavel')
    search_fields = ('titulo', 'docentes__nome')

    def listar_docente(self, obj):
        return ", ".join([docente.nome for docente in obj.docentes.all()])

    listar_docente.short_description = "Docentes"

    def link_clicavel(self, obj):
        if not obj.link_deisi:
            return "-"
        else:
            return format_html('<a href="{}" target="_blank">Abrir</a>', obj.link_deisi)
    
    link_clicavel.short_description = "Link DEISI"

class UcAdmin(admin.ModelAdmin):
    list_display = ('nome', 'titulo_projeto', 'listar_docente')
    search_fields = ('nome',)

    def listar_docente(self, obj):
        return ", ".join([docente.nome for docente in obj.docentes.all()])

    listar_docente.short_description = "Docentes"

    def titulo_projeto(self, obj):
        return obj.projeto_final
    
    titulo_projeto.short_description = "Projeto Final"

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'listar_ucs', 'listar_docente')
    search_fields = ('nome',)

    def listar_docente(self, obj):
        return ", ".join([docente.nome for docente in obj.docentes.all()])

    listar_docente.short_description = "Docentes"

    def listar_ucs(self, obj):
        ucs = obj.ucs.all()
        if not ucs:
            return '-'
        else:
            return ", ".join([uc.nome for uc in obj.ucs.all()])
    
    listar_ucs.short_description = "UCs"

class MakingOFAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'mostrar_arquivo', 'resumo')
    search_fields = ('titulo',)

    def mostrar_arquivo(self, obj):
        if obj.arquivo:
            return format_html('<a href="{}" target="_blank">Abrir arquivo Word</a>', obj.arquivo.url)
        else:
            return "-"

    mostrar_arquivo.short_description = "Arquivo"
    

admin.site.register(Docente, DocenteAdmin)
admin.site.register(Competencia,CompetenciaAdmin)
admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Formacao, FormacaoAdmin)
admin.site.register(TFC, TFCAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(UC,UcAdmin)
admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(MakingOF, MakingOFAdmin)


