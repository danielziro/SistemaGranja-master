from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProveedorSemen(models.Model):
    nit = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return self.nit

    class Meta:
        ordering = ('nit', )
