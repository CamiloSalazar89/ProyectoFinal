from django.urls import path

from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path( 'home', views.home, name='home'),
    path('producto', views.producto, name='producto'),
    
]
