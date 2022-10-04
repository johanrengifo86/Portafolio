from django.contrib import admin
from .models import Servicio


# Register your models here.


 # Se crea esta clase para aparezcan los campos created y updated
class ServicioAdmin(admin.ModelAdmin):  
    readonly_fields = ('created', 'updated') # Registra Campos de solo lectura 

admin.site.register(Servicio, ServicioAdmin)
