from django.db import models

class Docente (models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    linkedin = models.URLField(blank=True)
    
    def __str__(self):
        return self.nome

class Competencia (models.Model):
    titulo = models.CharField(max_length=50,null=False,blank=False)
    resumo_basico = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Empresa (models.Model):
    nome = models.CharField(max_length=100, null = False, blank=False)
    data_comeco = models.DateField(null=False,blank=False)
    data_saida = models.DateField()
    competencias = models.ManyToManyField(Competencia)

    def __str__(self):
        return self.nome
    
class Formacao (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    resumo = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class TFC (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    docente_responsavel = models.ManyToManyField(Docente, null=False, blank= False)
    tecnologias_usadas = models.CharField(max_length=100, null=False, blank=False)
    resumo = models.CharField(max_length=500, null=False, blank=False)
    video_imagem = models.URLField()
    interesse = models.DecimalField(max_digits=2, decimal_places=1, null= False, blank=False)
    


    






