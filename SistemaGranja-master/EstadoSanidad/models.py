from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EstadoSanidad(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id_estado

    class Meta:
            ordering = ('id_estado', )
