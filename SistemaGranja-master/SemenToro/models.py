from __future__ import unicode_literals

from django.db import models
from Raza.models import Raza
from ProveedorSemen.models import ProveedorSemen

# Create your models here.
class SemenToro(models.Model):

    id_semen_toro = models.AutoField(primary_key=True)
    id_raza = models.ForeignKey(Raza, related_name='id_semen_raza')
    edad = models.IntegerField()
    id_proveedor = models.ForeignKey(ProveedorSemen,related_name='id_semen_proveedor')

    def __str__(self):
        return self.id_semen_toro

    class Meta:
        ordering = ('id_semen_toro', )
