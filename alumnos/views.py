from django.shortcuts import render, redirect
from .models import Alumnos
from .forms import FormAlumno
# Create your views here.
def mainpage(request):
    return render(request, 'base.html')

def list_students(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'list_student.html', {'alumnos' : alumnos})

def add_students(request):
    form = FormAlumno()
    if request.method=='POST':
        form=FormAlumno(request.POST)
        if form.is_valid():
            form.save()
        return mainpage(request)
    return render(request, 'add_student.html', {'form' : form})

def delete_students(request):
    return render(request, 'edit_student.html',{})


def edit_students(request):
    return render(request, 'edit_student.html',{})