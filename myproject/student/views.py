from django.shortcuts import render,redirect
from student.models import *
from student.forms import *

# Create your views here.
def home(request):
    student=Student.objects.all()
    context={'student_key' : student}
    return render(request, 'student/home.html', context)

def add_student(request):
    house_choices = Student._meta.get_field('school_house').choices
    
    context = {
        'house_choices': house_choices # NEW variable for the choices
    }
    return render(request, 'student/addstudent.html' ,context)

def addition(request):
    form = StudentForm(data=request.POST)
    house_choices = Student._meta.get_field('school_house').choices
    
    context = {
        'house_choices': house_choices ,# NEW variable for the choices
        'form' : form
    }
    if form.is_valid():
        form.save()
    else:
        return render(request, 'student/addstudent.html', context)
    return redirect('/student/')

def del_student(request, id):
    st = Student.objects.get(id=id)
    st.delete()
    return redirect('/student/')

def edit_student(request, id):
    student= Student.objects.get(id=id)
    house_choices = Student._meta.get_field('school_house').choices
    
    
    context = {
        'house_choices': house_choices, # NEW variable for the choices
        'student':student
    }
    return render(request,'student/editstudent.html',context)

def update_student(request, id):
    st = Student.objects.get(id=id)
    form = StudentForm(data=request.POST,instance=st)
    if form.is_valid():
        form.save()
    return redirect('/student/')