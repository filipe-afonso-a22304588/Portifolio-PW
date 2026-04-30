from django.urls import path
from . import views

urlpatterns = [
   path("ucs/", views.ucs_view, name='ucs'),
   path("ucs/<int:id>/", views.uc_view, name='uc'),
   path("projetos/", views.projetos_view, name='projetos'),
   path("projetos/<int:id>/", views.projeto_view, name='projeto'),
   path("licenciaturas/", views.licenciaturas_view, name='licenciaturas'),
   path("licenciaturas/<int:id>/", views.licenciatura_view, name='licenciatura'),
   path("docentes/<int:id>/", views.docente_view, name='docente'),
   path("empresas/", views.empresas_view, name='empresas'),
   path("tfcs/", views.tfcs_view, name='tfcs'),
   path('projetos/novo', views.novo_projeto_view, name="novo_projeto"),
   path("", views.ucs_view, name='ucs'),


]
