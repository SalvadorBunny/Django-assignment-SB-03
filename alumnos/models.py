from django.db import models

# Create your models here.
class Alumnos(models.Model):
    id=models.IntegerField(primary_key=True)
    nota1=models.IntegerField()
    nota2=models.IntegerField()
    nota3=models.IntegerField()
    nombre=models.CharField(max_length=50)
    fechaIngreso=models.DateField()
    carrera= models.CharField(max_length=50)