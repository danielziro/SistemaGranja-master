from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id_sexo

    class Meta:
        ordering = ('id_sexo', )
