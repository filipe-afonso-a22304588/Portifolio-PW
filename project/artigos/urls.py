from django.urls import path, include
from . import views

urlpatterns = [
   path("artigos/", views.artigos_view, name='artigos'),
   path("login/", views.login_view, name='login'),
   path("registo/", views.registo_view, name='registo'),
   path("conta/", views.account_view, name='conta'),
   path("logout/", views.logout_view, name='logout'),
   path("artigo/<int:id>/", views.artigo_view, name='artigo'),
   path('artigo/<int:artigo_id>/edita', views.edita_artigo_view,name="edita_artigo"),
   path('artigo/<int:artigo_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),
   path('artigo/novo', views.novo_artigo_view, name="novo_artigo"),
   path('artigos/<int:id>/like/', views.like_artigo, name='like_artigo'),
   path('artigos/<int:id>/comentario/', views.adicionar_comentario, name='adicionar_comentario'),


]