from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from Bovino.models import Bovino


# Create your models here.
class ControlMastitis(models.Model):
    id_control = models.AutoField(primary_key=True)
    id_bovino = models.ForeignKey(Bovino, db_constraint=True, swappable=True, related_name='id_control_bovino',default=None)
    cad = models.BooleanField()
    cai = models.BooleanField()
    cpd = models.BooleanField()
    cpi = models.BooleanField()
    fecha = models.DateTimeField(verbose_name='Fecha de control', default=datetime.now)

    def __str__(self):
        return self.id_control

    class Meta:
        ordering = ('id_control', )
