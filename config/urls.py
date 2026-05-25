from django.contrib import admin
from django.urls import path, include
from .views import inicio

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', inicio, name='inicio'),

    path('productos/', include('productos.urls')),
    path('ventas/', include('ventas.urls')),
    path('ingresos/', include('ingresos.urls')),
    path('gastos/', include('gastos.urls')),
    path('finanzas/', include('finanzas.urls')),

]