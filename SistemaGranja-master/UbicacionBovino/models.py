from __future__ import unicode_literals

from django.db import models
from Bovino.models import Bovino
from Espacio.models import Espacio

# Create your models here.
class UbicacionBovino(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    id_bovino = models.ForeignKey(Bovino, related_name='id_ubicacion_bovino')
    id_espacio = models.ForeignKey(Espacio, related_name='id_ubicacion_espacio')

    def __str__(self):
        return self.id_ubicacion

    class Meta:
        ordering = ('id_ubicacion', )
