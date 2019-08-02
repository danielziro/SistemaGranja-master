from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Alimento(models.Model):
    id_alimento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False)
    cantidad = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.id_alimento

    class Meta:
        ordering = ('id_alimento', )
