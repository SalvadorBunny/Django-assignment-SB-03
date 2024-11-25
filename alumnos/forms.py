from django import forms
from .models import Alumnos
from django.core import validators

class FormAlumno(forms.ModelForm):
    carreras_choices= [
        ('MECANICA','Mecanica'),
        ('ADMINISTRACION','Administracion'),
        ('INFORMATICA','Informatica'),
        ('CONSTRUCCION','Construccion')
    ]

    nombre = forms.CharField(
        label='title', 
        widget=forms.TextInput(attrs={"placeholder" : "your title"}),
        required=True
        )
    
    fechaIngreso= forms.DateField(
        label='Fecha de ingreso',
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"]
        )
    
    nota1 = forms.DecimalField(
        label='Nota1',
        required=True,
        min_value=1.0,
        max_value=7.0,
        decimal_places=1
        )
    
    nota2 = forms.DecimalField(
        label='Nota2',
        required=True,
        min_value=1.0,
        max_value=7.0,
        decimal_places=1
        )
    
    nota3 = forms.DecimalField(
        label='Nota3',
        required=True,
        min_value=1.0,
        max_value=7.0,
        decimal_places=1
        )
    
    carrera = forms.ChoiceField(
        choices= carreras_choices,
        widget=forms.Select(attrs={
            'class' : 'form-choices'
        }),
        label='title', 
        required=True
        )

    class Meta:
        model = Alumnos
        fields=('nombre','fechaIngreso','nota1','nota2','nota3','carrera')
