from django.shortcuts import render, HttpResponse

from carroCompras.carro import Carro


# Create your views here.
# Vistas del Proyecto web 

def home(request):

    carro = Carro(request)

    return render(request, "Proyecto_WebApp/home.html")



