from django.contrib import admin
from .models import Noticia
from .models import Pessoa
from .models import Tag
from .models import Comentario
from .models import Categoria
from .models import Foto
# Register your models here.

@admin.register(Noticia)
@admin.register(Pessoa)
@admin.register(Tag)
@admin.register(Comentario)
@admin.register(Categoria)
@admin.register(Foto)

class NoticiaAdmin(admin.ModelAdmin):
    pass
