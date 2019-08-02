from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=140)
    laboratorio = models.CharField(max_length=140)
    reg_ica = models.CharField(max_length=140)
    numeroLote = models.CharField(max_length=140)
    observacion = models.CharField(max_length=140)
    fechaVencimiento = models.DateTimeField()

    def __str__(self):
        return self.id_medicamento

    class Meta:
        ordering = ('id_medicamento', )
