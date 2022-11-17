from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio (request):
    return render(request, 'paginas/Inicio.html')

def producto(request):
    return render(request, 'producto/index.html')

def blog (request):
    return render(request, 'paginas/blog.html')

def contacto (request):
    return render(request, 'paginas/contacto.html')

def crear (request):
    return render(request, 'producto/crear.html')

def editar (request):
    return render(request, 'producto/editar.html')





    
