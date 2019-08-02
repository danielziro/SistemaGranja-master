from __future__ import unicode_literals

from django.db import models
from Bovino.models import Bovino
from datetime import datetime

# Create your models here.
class Medidas(models.Model):
    id_medida = models.AutoField(primary_key=True)
    id_bovino = models.ForeignKey(Bovino, db_constraint=True, swappable=True,related_name='id_medida_bovino')
    peso = models.DecimalField(max_digits=4,decimal_places=2,default=None)
    alzada = models.DecimalField(max_digits=4,decimal_places=2,default=None)
    fecha = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.id_medida

    class Meta:
        ordering = ('id_medida', )
