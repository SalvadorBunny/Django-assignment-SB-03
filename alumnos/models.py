from django.db import models


# Create your models here.
class Alumnos(models.Model):
    id=models.AutoField(primary_key=True)
    nota1=models.DecimalField(max_digits=10, decimal_places=2)
    nota2=models.DecimalField(max_digits=10, decimal_places=2)
    nota3=models.DecimalField(max_digits=10, decimal_places=2)
    nombre=models.CharField(max_length=50)
    fechaIngreso=models.DateField()
    carrera= models.CharField(max_length=50)