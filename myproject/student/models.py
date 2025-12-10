from django.db import models

# Create your models here.
house = (
    ("Red", "Red House"),
    ("Yellow", "Yellow House"),
    ("Blue", "Blue House"),
    ("Green", "Green House"),
)
class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=120)
    standard = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    school_house = models.CharField(max_length=255, choices=house)
    admission_date = models.DateField()
    dob = models.DateField(blank=True , null=True)
    address = models.TextField(blank=True, null=True)

