from django.db import models
from django.contrib.auth.models import User

class Artigo (models.Model):
    texto = models.CharField(max_length=200, null=False, blank=False)
    fotografia = models.ImageField(upload_to='media/', null=True,  blank=True)
    link = models.URLField(blank=True, null = True)
    data_criacao = models.DateField(blank=True)
    
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='artigos'
    )

    def __str__(self):
        return self.texto

