from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Alumnos
from .forms import FormAlumno
# Create your views here.
def mainpage(request):
    return render(request, 'base.html')

def list_students(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'list_students.html', {'alumnos' : alumnos})

def add_students(request):
    form = FormAlumno()
    if request.method=='POST':
        form=FormAlumno(request.POST)
        if form.is_valid():
            form.save()
        return inde(request)
    return render(request, 'add_student.html', {'form' : form})