from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ViaAplicacion(models.Model):
    id_via_apli = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id_via_apli

    class Meta:
        ordering = ('id_via_apli', )
