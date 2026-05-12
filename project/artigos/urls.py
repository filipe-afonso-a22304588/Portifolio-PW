from django.urls import path, include
from . import views

urlpatterns = [
   path("artigos/", views.artigos_view, name='artigos'),
   path("login/", views.login_view, name='login_artigo'),
   path("registo/", views.registo_view, name='registo_artigo'),
   path("conta/", views.account_view, name='conta_artigo'),
   path("logout/", views.logout_view, name='logout_artigo'),
   path("artigo/<int:id>/", views.artigo_view, name='artigo'),
   path('artigo/<int:artigo_id>/edita', views.edita_artigo_view,name="edita_artigo"),
   path('artigo/<int:artigo_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),
   path('artigo/novo', views.novo_artigo_view, name="novo_artigo"),
   path('artigos/<int:id>/like/', views.like_artigo, name='like_artigo'),
   path('artigos/<int:id>/comentario/', views.adicionar_comentario, name='adicionar_comentario'),


]