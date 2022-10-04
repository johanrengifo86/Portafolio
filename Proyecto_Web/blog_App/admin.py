from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated') # Campos de solo lectura 

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# Registro de las clases 
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)