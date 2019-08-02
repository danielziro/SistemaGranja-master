from django.contrib import admin
from .models import Granja

# Register your models here.
#admin.site.register(Granja)
@admin.register(Granja)
class AdminGranja(admin.ModelAdmin):
    list_display = ('id_granja','nombre','altitud',)
    list_filter = ('nombre',)
