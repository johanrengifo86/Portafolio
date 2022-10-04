from django.urls import path

from Proyecto_WebApp import views #Importación views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    # Urls para cada View
    path('', views.home, name="Home"),

]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)