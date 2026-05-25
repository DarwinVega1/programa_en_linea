from django.db import models
from productos.models import Producto


class Cliente(models.Model):

    documento = models.CharField(max_length=13, unique=True)
    nombres = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombres

class Venta(models.Model):

    METODOS_PAGO = [
        ('EFECTIVO', 'EFECTIVO'),
        ('TRANSFERENCIA', 'TRANSFERENCIA'),
        ('TARJETA', 'TARJETA'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        default=1
    )

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    total = models.DecimalField(max_digits=10, decimal_places=2)

    metodo_pago = models.CharField(
        max_length=20,
        choices=METODOS_PAGO
    )

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.producto)