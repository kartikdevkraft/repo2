from django.shortcuts import render,redirect
from student.models import *
from student.forms import * 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def custom_login_view(request):
    
    if request.user.is_authenticated:
        
        next_url = request.GET.get('next') or request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('/student/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")

            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('/student/')
        else:
        
            messages.error(request, "Invalid username or password.")

    context = {
        'next': request.GET.get('next')
    }
    return render(request, 'custom_login.html', context)

def custom_logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')

@login_required
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