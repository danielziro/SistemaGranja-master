# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
#from django.utils.translation import gettext as _

class InicioSesionForm(AuthenticationForm):
    class Meta:
        model = User
