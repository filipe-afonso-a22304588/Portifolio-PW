from django.urls import path, include
from . import views

urlpatterns = [
   path("artigos/", views.artigos_view, name='artigos'),
   path("login/", views.login_view, name='login'),
   path("registo/", views.registo_view, name='registo'),
   path("conta/", views.account_view, name='conta'),
   path("logout/", views.logout_view, name='logout'),
   path("artigo/<int:id>/", views.artigo_view, name='artigo'),


]