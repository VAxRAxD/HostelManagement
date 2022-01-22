from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializers import *
from . models import *

# Create your views here.
@api_view(('GET',))
def students(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data)

@api_view(('GET',))
def rooms(request):
    rooms=Room.objects.all()
    serializer=RoomSerializer(rooms,many=True)
    return Response(serializer.data)

@api_view(('GET',))
def studentDetails(request,id):
    student=Student.objects.get(id=id)
    serializer=StudentSerializer(student,many=False)
    return Response(serializer.data)

@api_view(('GET',))
def roomDetails(request,id):
    room=Room.objects.get(number=id)
    serializer=RoomSerializer(room,many=False)
    return Response(serializer.data)

@api_view(('GET',))
def deleteRoom(request,id):
    room=Room.objects.get(number=id)
    room.delete()
    return HttpResponse()

@api_view(('GET',))
def deleteStudent(request,id):
    student=Student.objects.get(id=id)
    if student.room:
        room_no=student.room.number
        room=Room.objects.get(number=room_no)
        room.Status="Empty"
        room.save()
        student.delete()
        return HttpResponse()
    else:
        student.delete()
        return HttpResponse()

@api_view(('GET',))
def mess(request):
    mess=Mess.objects.all()
    serializer=MessSerializer(mess,many=True)
    return Response(serializer.data)

@api_view(('GET','POST'))
def login(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        name=data[0]
        password=data[1]
        student=Student.objects.get(name=name)
        if student and student.password==password:
            validate=[{
                    'validation':'pass'
                }]
        else:
            validate=[{
                    'validation':'fail'
                }]
        return Response(validate)
        
    else:
        data=[{
            'method':'Get'
        }]
        return Response(data)
@api_view(('GET','POST'))
def studentUpdate(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        name=data[0]
        email=data[1]
        address=data[2]
        phone=data[3]
        room=data[4]
        hostel_fees=data[5]
        mess_fees=data[6]
        attendance=data[7]
        student=Student.objects.get(name=name)
        if student:
            student.email=email
            student.address=address
            student.phone=phone
            if hostel_fees=="Paid":
                student.hostel_fees=True
            else:
                student.hostel_fees=False
            if mess_fees=="Paid":
                student.mess_fees=True
            else:
                student.mess_fees=False
            student.attendnace=attendance
            student.save()
            data=[{
            'update':'pass'
            }]
        else:
            data=[{
            'update':'fail'
            }]
        return Response(data)
    else:
        data=[{
            'method':'Get'
        }]
        return Response(data)