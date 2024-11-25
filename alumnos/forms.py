from django import forms
from .models import Alumnos
class FormAlumno(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields="__all__"
