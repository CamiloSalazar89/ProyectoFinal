from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto', views.producto, name='producto'),
    path('blog', views.blog, name='blog'),
    path('contacto', views.contacto, name='contacto'),
    path('producto/crear', views.crear, name='crear'),
    path('producto/editar', views.editar, name='editar'),

    
]

