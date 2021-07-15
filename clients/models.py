from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    ID_fiscal = models.CharField(max_length=200, null=False)
    nombres = models.CharField(max_length=200, null=False)
    apellidos = models.CharField(max_length=200, null=False)
    empresa = models.CharField(max_length=200)
    correo = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    contacto = models.CharField(max_length=200)
    telefono_contacto = models.CharField(max_length=200)
    mail_contacto = models.EmailField(max_length=200)
    pais = models.CharField(max_length=100, null=True)
    activo = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField('date published', default = timezone.now)
    fecha_inactivo = models.DateTimeField('desactived date', null=True)
    def __str__(self):
        return self.ID_fiscal


