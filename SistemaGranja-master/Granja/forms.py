from django import forms
from .models import Granja

class GranjaForm(forms.ModelForm):
    class Meta:
        model = Granja
        fields = '__all__'
