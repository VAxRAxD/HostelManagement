from rest_framework.serializers import ModelSerializer,SerializerMethodField
from . models import *

class StudentSerializer(ModelSerializer):
    room_number=SerializerMethodField("get_number")
    hostel_fees=SerializerMethodField("get_hostel_fees")
    mess_fees=SerializerMethodField("get_mess_fees")
    class Meta:
        model=Student
        fields=['name','email','address','phone','room_number','hostel_fees','mess_fees','attendance']
    def get_number(self,Student):
        if Student.room:
            return Student.room.number
        return "None"
    def get_hostel_fees(self,Student):
        if Student.hostel_fees:
            return "Paid"
        return "Pending"
    def get_mess_fees(self,Student):
        if Student.mess_fees:
            return "Paid"
        return "Pending"

class RoomSerializer(ModelSerializer):
    student_name= SerializerMethodField('get_name')
    class Meta:
        model=Room
        fields=['number','status','student_name']
    def get_name(self,Room):
        if Room.student:
            return Room.student.name
        return "None"

class MessSerializer(ModelSerializer):
    class Meta:
        model=Mess
        fields=['name','category']