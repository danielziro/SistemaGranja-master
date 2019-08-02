from __future__ import unicode_literals

from django.db import models
from EstadoSanidad.models import EstadoSanidad
from Medicamento.models import Medicamento
from Bovino.models import Bovino
from ViaAplicacion.models import ViaAplicacion
from ControlMastitis.models import ControlMastitis


# Create your models here.
class Sanidad(models.Model):
    id_sanidad = models.AutoField(primary_key=True)
    id_estado = models.OneToOneField(EstadoSanidad, related_name='id_sanidad_estado')
    id_control =  models.ForeignKey(ControlMastitis, related_name='id_sanidad_control')
    id_bovino = models.ForeignKey(Bovino, related_name='id_sanidad_bovino')
    id_medicamento = models.OneToOneField(Medicamento, related_name='id_sanidad_medicamento')
    id_via_apli = models.ForeignKey(ViaAplicacion, related_name='id_sanidad_via')
    peso_vivo_prom = models.DecimalField(max_digits=10,decimal_places=2)
    evento = models.CharField(max_length=50)
    dosis = models.IntegerField()
    tiempo_retiro = models.IntegerField()
    fecha_aplicacion = models.DateTimeField()

    def __str__(self):
        return self.id_sanidad

    class Meta:
            ordering = ('id_sanidad', )
