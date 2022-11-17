from django.urls import path

from . import views

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('producto', views.producto, name='producto'),
    path('blog', views.blog, name='blog'),
    path('contacto', views.contacto, name='contacto'),
    
]

