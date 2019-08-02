from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Etapa(models.Model):
    id_etapa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id_etapa

    class Meta:
        ordering = ('id_etapa', )
