from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_gastos, name='lista_gastos'),
    path('nuevo/', views.nuevo_gasto, name='nuevo_gasto'),
]