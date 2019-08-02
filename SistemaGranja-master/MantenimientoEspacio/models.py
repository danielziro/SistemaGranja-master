from __future__ import unicode_literals

from django.db import models
from Espacio.models import Espacio

# Create your models here.
class MantenimientoEspacio(models.Model):
    id_mant_espacio = models.AutoField(primary_key=True)
    id_espacio = models.ForeignKey(Espacio, related_name='id_mant_espacio')
    diasDescanso = models.IntegerField()
    cantPorquinaza = models.DecimalField(decimal_places=2,max_digits=10)
    cantBovinaza = models.DecimalField(decimal_places=2,max_digits=10)
    cantUrea = models.DecimalField(decimal_places=2,max_digits=10)
    controlPlagas =  models.IntegerField()
    cantCalDol = models.DecimalField(decimal_places=2,max_digits=10)
    regarEstiercol =  models.IntegerField()
    controlMaleza =  models.IntegerField()
    guadana =  models.IntegerField()
    fecha = models.DateTimeField()

    def __str__(self):
        return self.id_mant_espacio

    class Meta:
            ordering = ('id_mant_espacio', )
