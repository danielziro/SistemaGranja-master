from __future__ import unicode_literals

from django.db import models
from Granja.models import Granja

# Create your models here.
class EntregaLeche(models.Model):
    id_ent_leche = models.AutoField(verbose_name='Identificacion entrega de leche',primary_key=True)
    volumen = models.DecimalField(decimal_places=2, max_digits=10)
    fechaEntrega = models.DateTimeField(default=None)
    placaVehiculo = models.CharField(max_length=10)
    nombreConductor = models.CharField(max_length=140)
    responsableEntrega = models.CharField(max_length=140)
    temperaturaLeche = models.DecimalField(decimal_places=2, max_digits=4)
    id_granja = models.ForeignKey(Granja, related_name='id_entrega_granja')

    def __str__(self):
        return self.id_ent_leche

    class Meta:
        ordering = ('id_ent_leche', )
