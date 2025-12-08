from django.db import models

# Create your models here.
Designation = (
    ("HR", "HR"),
    ("pdev", "Python Developer"),
    ("jdev", "Java Developer"),
    ("cdev", "C++ Developer"),
    ("Software Engineer", "Software Engineer"),
    ("QA Engineer", "QA Engineer"),
    ("Project Manager", "Project Manager"),
)
class Employee(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=255, choices=Designation)
    joining_date = models.DateField()
    dob = models.DateField(blank=True , null=True)
    address = models.TextField(blank=True, null=True)
