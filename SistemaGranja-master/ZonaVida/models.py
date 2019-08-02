from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ZonaVida(models.Model):
    id_zona_vida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id_zona_vida', )
