from django.db import models
from productos.models import Producto


class Ingreso(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)

    talla = models.CharField(max_length=50)

    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto.codigo} - {self.producto.nombre}"