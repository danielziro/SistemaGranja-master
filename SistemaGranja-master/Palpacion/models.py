from __future__ import unicode_literals

from django.db import models
from EstadoPalpacion.models import EstadoPalpacion
from Reproduccion.models import Reproduccion

# Create your models here.
class Palpacion(models.Model):
    id_palpacion = models.AutoField(primary_key=True)
    id_reproduccion = models.ForeignKey(Reproduccion, related_name='id_palpacion_reproduccion')
    id_estado = models.OneToOneField(EstadoPalpacion,related_name='id_palpacion_estado')
    observacion = models.CharField(max_length=140)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.id_palpacion

    class Meta:
        ordering = ('id_palpacion', )
