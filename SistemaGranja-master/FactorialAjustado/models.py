from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FactorialAjustado(models.Model):
    id_factorial = models.AutoField(primary_key=True)
    dias = models.IntegerField()
    factor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id_factorial

    class Meta:
        ordering = ('id_factorial', )
