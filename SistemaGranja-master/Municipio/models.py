from __future__ import unicode_literals

from django.db import models
from Departamento.models import Departamento

# Create your models here.
class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_departamento = models.OneToOneField(Departamento, related_name='id_municipio_departamento', default=None)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ('id_municipio', )
