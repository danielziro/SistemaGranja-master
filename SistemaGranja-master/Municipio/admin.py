from django.contrib import admin
from .models import Municipio
# Register your models here.
@admin.register(Municipio)
class AdminMunicipio(admin.ModelAdmin):
    list_display = ('id_municipio','nombre',)
    list_filter = ('nombre',)
