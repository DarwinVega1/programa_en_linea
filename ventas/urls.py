from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ventas, name='lista_ventas'),
    path('nuevo/', views.nueva_venta, name='nueva_venta'),
]