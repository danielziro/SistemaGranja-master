from __future__ import unicode_literals

from django.db import models
from Granja.models import Granja
from TipoEspacio.models import TipoEspacio
from EstadoEspacio.models import EstadoEspacio

# Create your models here.
class Espacio(models.Model):
    id_espacio = models.AutoField(primary_key=True)
    id_estado = models.OneToOneField(EstadoEspacio, related_name='id_espacio_estado')
    id_granja = models.ForeignKey(Granja, related_name='id_espacio_granja')
    id_tipo = models.OneToOneField(TipoEspacio, related_name='id_espacio_tipo')
    area = models.DecimalField(decimal_places=2,max_digits=10)
    capacidad = models.IntegerField()
    nombre = models.CharField(max_length=50)
    aforo = models.DecimalField(decimal_places=2,max_digits=10)
    porcentaje_desperdicio = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.id_espacio

    class Meta:
        ordering = ('id_espacio', )
