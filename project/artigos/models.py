from django.db import models
from django.contrib.auth.models import User

class Artigo (models.Model):
    texto = models.CharField(max_length=200, null=False, blank=False)
    fotografia = models.ImageField(upload_to='media/', null=True,  blank=True)
    link = models.URLField(blank=True, null = True)
    data_criacao = models.DateField(blank=True)

    likes = models.ManyToManyField(
        User,
        related_name='artigos_com_like',
        blank=True
    )

    def total_likes(self):
        return self.likes.count()

    
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='artigos'
    )

    def __str__(self):
        return self.texto


class Comentario(models.Model):

    artigo = models.ForeignKey(
        Artigo,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    texto = models.TextField()

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} - {self.artigo}"
