from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"

    def __unicode__(self):
        return self.id_raza
