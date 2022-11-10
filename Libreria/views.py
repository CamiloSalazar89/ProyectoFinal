from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio (request):
    return render(request, 'paginas/Inicio.html')

def home (request):
    return render(request, 'paginas/Home.html')

def producto(request):
    return render(request, 'producto/index.html')

