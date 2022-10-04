from django.contrib import admin
from .models import CategoriaProducto, Producto

# Register your models here.

# Se especifica que los campos created y updated de los modelos son de solo lectura
class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

# Registro de modelos 

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)


