from pickle import FALSE
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100, null=True, unique=True)
    email=models.EmailField(unique=True)
    address=models.TextField(null=True)
    phone=models.CharField(max_length=10,null=True)
    room=models.ForeignKey("Room",null=True,blank=True,related_name='room_details',on_delete=models.SET_NULL)

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

