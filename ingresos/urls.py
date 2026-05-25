from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ingresos, name='lista_ingresos'),
    path('nuevo/', views.nuevo_ingreso, name='nuevo_ingreso'),
    path('editar/<int:id>/', views.editar_ingreso, name='editar_ingreso'),
]