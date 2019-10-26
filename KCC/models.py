from django.db import models

# Create your models here.
class KCC(models.Model):
    NombreCliente = models.CharField(max_length=200, verbose_name="Nombre Cliente")
    Latitud = models.FloatField()
    Longitud = models.FloatField()
    Domicilio = models.CharField(max_length=200, verbose_name="Dirección")
    Foto= models.CharField(max_length=200, null=True, blank=True)
    Pedido = models.TextField()
    Precio = models.FloatField()

    def __str__(self):
        return self.NombreCliente