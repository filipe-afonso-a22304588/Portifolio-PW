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


class Tecnologia (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao =  models.CharField(max_length=200, null = True)
    exemplos_uso =  models.CharField(max_length=200, null=True)
    docente = models.ManyToManyField(Docente, null=False, blank=False)
    logo = models.ImageField(upload_to='logos/', null=True)

class Projeto (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    docentes = models.ManyToManyField(Docente, null=False, blank=False)
    nota_final = models.DecimalField(max_digits=2, decimal_places=1, null= False, blank=False)
    tecnologias_usadas = models.ManyToManyField(Tecnologia, null=False,blank=False)
    descricao = models.CharField(max_length=200)
    exemplo = models.ImageField(upload_to='projetos/', null=True)
    link_deisi = models.URLField(null=True)

class UC (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    docentes = models.ManyToManyField(Docente, null=False,blank=False)
    tecnologias_aprendidas = models.ManyToManyField(Tecnologia, null=False,blank=False)
    projeto_final = models.OneToOneField(Projeto, null=True, on_delete=models.SET_NULL)
    resumo = models.CharField(max_length=100)

class Licenciatura (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    ucs = models.ManyToManyField(UC, null=False,blank=False)
    objetivos = models.CharField(max_length=500)
    docentes = models.ManyToManyField(Docente, null=False, blank=False)
    tecnologias = models.ManyToManyField(Tecnologia, null=False, blank=False)

    






