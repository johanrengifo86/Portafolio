from tabnanny import verbose
from venv import create
from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) # Inserta de forma automatica la fecha de creacion
    updated = models.DateTimeField(auto_now_add=True) # Inserta de forma automatica la fecha de actualizacion

    # Especifica el nombre en singular y plural la categoria  
    class Meta:
        verbose_name = "categoria_producto"
        verbose_name_plural = "categorias_producto"

    # Devuelve el nombre de la categoria 
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    # clave foranea, se especifica la tabla de relacion, y se especifica la eliminacion en cascada 
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= "tienda", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    
