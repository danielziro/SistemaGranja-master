from django.contrib import admin
from .models import Departamento
# Register your models here.
@admin.register(Departamento)
class AdminDepartamento(admin.ModelAdmin):
    list_display = ('id_departamento','nombre',)
    list_filter = ('nombre',)
