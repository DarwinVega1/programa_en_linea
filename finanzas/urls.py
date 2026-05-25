from django.urls import path
from .views import dashboard_finanzas

urlpatterns = [

    path('', dashboard_finanzas),

]