from django.shortcuts import render, redirect
from .models import Alumnos
from .forms import FormAlumno
# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html')

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

def delete_students(request, id):
    alumnos= Alumnos.objects.get(id=id)
    alumnos.delete()
    return select_student_delete(request)

def select_student(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'edit_student.html', {'alumnos' : alumnos})

def select_student_delete(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'delete_student.html', {'alumnos' : alumnos})

def edit_students(request, id):
    alumnos = Alumnos.objects.get(id=id)
    form=FormAlumno(instance=alumnos)
    if request.method == 'POST':
        form=FormAlumno(request.POST, instance=alumnos)
        if form.is_valid():
            form.save()
        return redirect('list_student')
    return render(request, 'add_student.html',{'form' : form })

def search_student(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        alumnos = Alumnos.objects.filter(id__contains= searched)
        return render(request,
                      'list_student.html',
                      {'searched': searched,
                       'alumnos' : alumnos
                       })
    else:
        return redirect('mainpage')