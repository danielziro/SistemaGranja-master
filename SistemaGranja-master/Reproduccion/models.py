from __future__ import unicode_literals

from django.db import models
from Servicio.models import Servicio
from SemenToro.models import SemenToro
from Bovino.models import Bovino

# Create your models here.
class Reproduccion(models.Model):
    id_reproduccion = models.AutoField(primary_key=True)
    id_bovino = models.ForeignKey(Bovino, db_constraint=True, swappable=True, related_name='id_reproduccion_bovino')
    id_toro = models.ForeignKey(Bovino, db_constraint=True, swappable=True, related_name='id_reproduccion_toro')
    id_servicio = models.OneToOneField(Servicio, related_name='id_reproduccion_servicio')
    id_cria = models.ForeignKey(Bovino, db_constraint=True, swappable=True, related_name='id_reproduccion_cria')
    id_semen_toro = models.ForeignKey(SemenToro, db_constraint=True, swappable=True, related_name='id_reproduccion_semen')
    fecha_servicio = models.DateTimeField()
    proximoCelo = models.DateTimeField()
    fechaPosibleParto = models.DateTimeField()
    fechaSecado = models.DateTimeField()

    def __str__(self):
        return self.id_reproduccion

    class Meta:
        ordering = ('id_reproduccion', )
