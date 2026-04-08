from django.db import models

class Docente (models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    link = models.URLField(blank=True, null = True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome

class Competencia (models.Model):
    titulo = models.CharField(max_length=50,null=False,blank=False)
    resumo_basico = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo

class Empresa (models.Model):
    nome = models.CharField(max_length=100, null = False, blank=False)
    data_comeco = models.DateField(null=False,blank=False)
    data_saida = models.DateField(null=True, blank=True)
    competencias = models.ManyToManyField(Competencia, blank=True)

    def __str__(self):
        return self.nome
    
class Formacao (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    resumo = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo
    
class TFC (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    docente_responsavel = models.CharField(blank= True)
    tecnologias_usadas = models.CharField(max_length=100, null=False, blank=False)
    resumo = models.CharField(max_length=500, blank=True)
    video_imagem = models.URLField(blank=True)
    interesse = models.DecimalField(max_digits=2, decimal_places=1, null= False, blank=False)

    def __str__(self):
        return self.titulo

class Tecnologia (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao =  models.CharField(max_length=200, null = True)
    exemplos_uso =  models.CharField(max_length=200, null=True)
    docente = models.ManyToManyField(Docente, blank=True)
    logo = models.ImageField(upload_to='logos/', null=True,  blank=True)

    def __str__(self):
        return self.nome

class Projeto (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    docentes = models.ManyToManyField(Docente, blank=False)
    nota_final = models.DecimalField(max_digits=3, decimal_places=1, null= False, blank=False)
    tecnologias_usadas = models.ManyToManyField(Tecnologia, blank=False)
    descricao = models.CharField(max_length=200)
    exemplo = models.ImageField(upload_to='projetos/', null=True, blank=True)
    link_deisi = models.URLField(null=True ,blank=True)

    def __str__(self):
        return self.titulo

class UC (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    docentes = models.ManyToManyField(Docente, blank=False)
    tecnologias_aprendidas = models.ManyToManyField(Tecnologia, blank=False)
    projeto_final = models.OneToOneField(Projeto, null=True, on_delete=models.SET_NULL, blank=True)
    resumo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Licenciatura (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    ucs = models.ManyToManyField(UC, blank=True)
    objetivos = models.CharField(max_length=500, blank=True)
    docentes = models.ManyToManyField(Docente, blank=False)
    tecnologias = models.ManyToManyField(Tecnologia, blank=False)

    def __str__(self):
        return self.nome

class MakingOF (models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    resumo = models.CharField(max_length=100, blank=True)
    arquivo = models.FileField(upload_to='documentos/', blank = True)
    imagem = models.ImageField(upload_to='makingOF/',  blank=True)

    def __str__(self):
        return self.titulo
    






