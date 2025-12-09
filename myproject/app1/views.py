from django.shortcuts import render, redirect
from app1.models import Employee
from app1.forms import EmployeeForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


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
    