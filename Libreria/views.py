from django.shortcuts import render
from django.http import HttpResponse
from .models import Juguetes
from .models import Alimentacion
from .models import Accesorios

# Create your views here.

def inicio (request):
    return render(request, 'paginas/Inicio.html')

def producto(request):
    Juguetes = Juguetes.objects.all()
    Alimentacion = Alimentacion.objects.all()
    Accesorios = Accesorios.objects.all()
   
    return render(request, 'producto/index.html', {'Juguetes': Juguetes , 'Alimentacion': Alimentacion  , 'Accesorios': Accesorios})

def blog (request):
    return render(request, 'paginas/blog.html')

def contacto (request):
    return render(request, 'paginas/contacto.html')

def crear (request):
    return render(request, 'producto/crear.html')

def editar (request):
    return render(request, 'producto/editar.html')




    
