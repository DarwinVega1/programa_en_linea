from django.db import models

class Producto(models.Model):

    codigo = models.CharField(max_length=50)

    nombre = models.CharField(max_length=200)

    talla = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    stock = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"