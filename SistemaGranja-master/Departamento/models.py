from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id_departamento', )
