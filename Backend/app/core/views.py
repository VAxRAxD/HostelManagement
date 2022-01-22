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
    student.delete()
    return HttpResponse()

@api_view(('GET',))
def mess(request):
    mess=Mess.objects.all()
    serializer=MessSerializer(mess,many=True)
    return Response(serializer.data)

def login(request):
    if request.method=="POST":
        pass
    else:
        return HttpResponse("Im-Getter")