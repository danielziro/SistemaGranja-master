from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id_servicio

    class Meta:
        ordering = ('id_servicio', )
