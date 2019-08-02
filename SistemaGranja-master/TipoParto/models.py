from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TipoParto(models.Model):
    id_parto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.id_parto

    class Meta:
        ordering = ('id_parto', )
