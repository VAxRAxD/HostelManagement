from email.policy import default
from pickle import FALSE
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100, null=True, unique=True)
    email=models.EmailField(unique=True)
    address=models.TextField(null=True)
    phone=models.CharField(max_length=10,null=True)
    room=models.ForeignKey("Room",null=True,blank=True,related_name='room_details',on_delete=models.SET_NULL)
    attendance=models.CharField(max_length=10,default="000.000")
    hostel_fees=models.BooleanField(default=False)
    mess_fees=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Room(models.Model):
    student=models.ForeignKey(Student,null=True,blank=True,related_name='student_details',on_delete=models.SET_NULL)
    number = models.IntegerField(primary_key=True)
    STATUS=(
			('Occupied', 'Occupied'),
			('Empty', 'Empty'),
			)
    status=models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.number)

class Mess(models.Model):
    CATEGORY=(
        ('VEG','VEG'),
        ('NON-VEG','NON-VEG'),
    )
    name=models.CharField(max_length=100,null=True,unique=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)

    def __str__(self):
        return self.name

