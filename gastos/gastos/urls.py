from django.urls import path
from .views import lista_gastos, nuevo_gasto

urlpatterns = [

    path('', lista_gastos),

    path('nuevo/', nuevo_gasto),

]