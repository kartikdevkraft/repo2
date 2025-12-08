from django.shortcuts import render
from app1.models import Employee

# Create your views here.
def employee_list(request):
    employees= Employee.objects.all()
    name = 'CompanyXYZ'
    return render(request ,'employees.html', context={'employees_key' : employees,
                                                      'name' : name
                                                      })



