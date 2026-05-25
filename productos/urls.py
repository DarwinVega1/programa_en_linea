from django.urls import path
from .views import lista_productos, nuevo_producto

urlpatterns = [
    path('', lista_productos),
    path('nuevo/', nuevo_producto),
    path('', lista_productos, name='lista_productos'),
]