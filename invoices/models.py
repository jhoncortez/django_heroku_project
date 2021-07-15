from django.db import models
from django.utils import timezone

class Factura(models.Model):
    ID_fiscal = models.CharField(max_length=200, null=False)
    cliente = models.ForeignKey("clients.Cliente", on_delete=models.CASCADE, null=True)
    fecha_factura = models.DateTimeField('date published', default = timezone.now)
    valor_factura = models.FloatField(default=0.0)
    moneda = models.CharField(max_length=10)
    estado_factura = models.IntegerField(default=1)
    pais_factura = models.CharField(max_length=100)
    def __str__(self):
        return self.ID_fiscal