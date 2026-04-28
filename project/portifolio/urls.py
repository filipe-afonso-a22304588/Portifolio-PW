from django.urls import path
from . import views

urlpatterns = [
   path("uc/", views.uc_view, name='ucs'),
]
