from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    usuario = models.OneToOneField(User, on_delete= models.CASCADE, verbose_name= 'Usuário')
    nome = models.CharField('Nome', max_length= 128)
    data_de_nascimento = models.DateField('Data de nascimento', blank = True)
    telefone_celular = models.CharField('Telefone celular', max_length = 15, help_text = 'Numero do telefone celular no formato (99) 99999-9999', null = True, blank= True)
    telefone_fixo = models.CharField('Telefone fixo', max_length = 15, help_text = 'Numero do telefone fixo no formato (99) 9999-9999', null = True, blank= True)
    email = models.EmailField('E-mail', null = True, blank = True)

    def __str__(self):
        return self.nome
    
    pass

class Tag(models.Model):
    nome = models.CharField(max_length = 64)
    slug = models.SlugField(max_length = 64)


    def __str__(self):
        return self.nome

class Categoria(models.Model):
    titulo = models.CharField("titulo", max_length = 64, blank = True, null = True)

    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    conteudo = models.TextField()
    data_publicacao = models.DateField('data publicação', max_length=128, blank=True, null=True)
    titulo = models.CharField('titulo', max_length=128, blank=True, null=True)
    autor = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    categoria =  models.ForeignKey(Categoria, on_delete = models.CASCADE, blank = True, null = True)
    foto = models.ForeignKey(Foto, on_delete = models.CASCADE, blank = True, null = True)
    
    def __str__(self):
        return self.titulo
   
    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

class Comentario(models.Model):
    comentarios = models.TextField()
    pessoas = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True, null=True)
    data_hora = models.DateTimeField('data e hora do comentario', blank = True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comentarios

class Foto(models.Model):
    titulo = models.CharField('Titulo', max_length = 64 , blank = True, null = True)
    url = models.SlugField(max_length = 64)



    


    