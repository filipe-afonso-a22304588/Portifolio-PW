from django.urls import path
from . import views

urlpatterns = [
   path("ucs/", views.ucs_view, name='ucs'),
   path("projetos/", views.projetos_view, name='projetos'),
   path("projetos/<int:id>/", views.projeto_view, name='projeto'),


]
