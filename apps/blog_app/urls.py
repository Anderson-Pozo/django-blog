from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('tecnologia/', tecnologia, name = 'tecnologia'),
    path('programacion/', programacion, name = 'programacion'),
    path('actualidad/', actualidad, name = 'actualidad'),
    path('contacto/', contacto, name = 'contacto'),
    #url detalle post
    path('<slug:slug>/<int:id>/', detallePost, name = 'detalle_post'),
    #url detalle autor
    path('<int:id>/', autor, name = 'autor'),

    
]