from django.contrib import admin
from .models import ZonaVida
# Register your models here.
@admin.register(ZonaVida)
class AdminZonaVida(admin.ModelAdmin):
    list_display = ('id_zona_vida','nombre',)
    list_filter = ('nombre',)
