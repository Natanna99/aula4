from django.db import models

# Create your models here.
class Noticia(models.Model):
    conteudo = models.TextField()
    data_publicacao = models.DateField('data publicação', max_length=128, blank=True, null=True)
    titulo = models.CharField('titulo', max_length=128, blank=True, null=True)
    auto = models.CharField('autor', max_length=128, blank=True, null=True)
    
    def __str__(self):
        return self.titulo
   
    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
    
    