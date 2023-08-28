from django.urls import path
from galeria.views import buscar, index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem,  name='imagem'), #seleciona imagem dinamicamente
    path("buscar", buscar, name="buscar"),
]