from django.shortcuts import render, redirect
from app1.models import Employee
from app1.forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

def custom_login_view(request):
    
    if request.user.is_authenticated:
        
        next_url = request.GET.get('next') or request.POST.get('next')
        if next_url:
            return redirect(next_url)
        return redirect('/employee/')
    
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
            return redirect('/employee/')
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

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def employee_list(request):
    employees= Employee.objects.all()
    name = 'CompanyXYZ'
    return render(request ,'employees.html', context={'employees_key' : employees,
                                                      'name' : name
                                                      })


def edit_emp(request, id):
    employee= Employee.objects.get(id=id)
    designation_choices = Employee._meta.get_field('designation').choices
    
    
    context = {
        'designation_choices': designation_choices, # NEW variable for the choices
        'employee':employee
    }
    return render(request,'editemployee.html',context)

def add_emp(request):
    designation_choices = Employee._meta.get_field('designation').choices
    
    context = {
        'designation_choices': designation_choices # NEW variable for the choices
    }
    return render(request,'addemployee.html', context)


def update_emp(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(data=request.POST,instance=emp)
    if form.is_valid():
        form.save()
    return redirect('/employee/')

def delete_emp(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/employee/')

def addition(request):
    form = EmployeeForm(data=request.POST)
    if form.is_valid():
        form.save()
    else:
        return render(request, 'addemployee.html', context={'form' : form})
    return redirect('/employee/')
    