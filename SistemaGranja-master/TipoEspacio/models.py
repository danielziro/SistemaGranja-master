from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TipoEspacio(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id_tipo

    class Meta:
        ordering = ('id_tipo', )
