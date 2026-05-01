from django import forms   
from .models import Projeto, Tecnologia, Competencia, Formacao, Docente
from django_select2.forms import ModelSelect2MultipleWidget

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto   
    fields = '__all__'
     
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

       # ordenar alfabeticamente
      self.fields['docentes'].queryset = Docente.objects.all().order_by('nome')
      self.fields['tecnologias_usadas'].queryset = Tecnologia.objects.all().order_by('nome')

class TecnologiaForm(forms.ModelForm):
  class Meta:
    model = Tecnologia   
    fields = '__all__'