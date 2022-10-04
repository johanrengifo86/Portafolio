from django.urls import path
from .views import VRegistro, cerrar_sesion, login, loguear #Importación views


urlpatterns = [
   
    # Urls para cada View

    path('', VRegistro.as_view(), name="Autenticacion"),

    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),

    path('loguear', loguear, name="loguear"),
]