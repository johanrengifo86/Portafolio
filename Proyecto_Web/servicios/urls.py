from django.urls import path

from . import views #Importación views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    # Urls para cada View
    
    path('', views.servicios, name="Servicios"),
    
]
