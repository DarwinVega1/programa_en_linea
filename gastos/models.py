from django.db import models

class Gasto(models.Model):

    TIPOS = [

        ('ARRIENDO', 'ARRIENDO'),

        ('EMPLEADOS', 'EMPLEADOS'),

        ('SERVICIOS', 'SERVICIOS'),

        ('PUBLICIDAD', 'PUBLICIDAD'),

        ('COMPRAS', 'COMPRAS'),

        ('OTROS', 'OTROS'),

    ]

    tipo = models.CharField(max_length=50, choices=TIPOS)

    descripcion = models.CharField(max_length=200)

    valor = models.DecimalField(max_digits=10, decimal_places=2)

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.descripcion