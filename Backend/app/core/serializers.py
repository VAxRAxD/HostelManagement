from rest_framework.serializers import ModelSerializer,SerializerMethodField
from . models import *

class StudentSerializer(ModelSerializer):
    room_number=SerializerMethodField("get_number")
    class Meta:
        model=Student
        fields=['name','email','address','phone','room_number']
    def get_number(self,Student):
        if Student.room:
            return Student.room.number
        return "None"

class RoomSerializer(ModelSerializer):
    student_name= SerializerMethodField('get_name')
    class Meta:
        model=Room
        fields=['number','status','student_name']
    def get_name(self,Room):
        if Room.student:
            return Room.student.name
        return "None"