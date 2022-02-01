from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializers import *
from . models import *
from . urls import *

# Create your views here.
@api_view(('GET',))
def routes(request):
    ROUTES=[{
        "admin/": "Admin Page",
        "students/": "Students Details",
        "rooms/": "Room Details",
        "mess/": "Mess Details",
        "login/": "Login",
        "register/": "Register",
        "students/<str:id>/": "Specific Student Details",
        "rooms/<str:id>/": "Specific Room Details",
        "rooms/delete/<str:id>/": "Delete a Room",
        "students/delete/<str:id>/": "Delete a Student",
        "student/update/": "Update Details of Student",
        "hostelfees/<str:id>/": "Pay Hostel Fees",
        "messfees/<str:id>/": "Pay Mess Fees"
    }]
    return Response(ROUTES)

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
    if room:
        data=[{
                'deletion':'pass'
            }]
        room.delete()
        return Response(data)
    else:
        data=[{
                'deletion':'fail'
            }]
        return Response(data)


@api_view(('GET',))
def deleteStudent(request,id):
    student=Student.objects.get(id=id)
    if student:
        if student.room:
            room_no=student.room.number
            room=Room.objects.get(number=room_no)
            room.status="Empty"
            room.save()
            student.delete()
            data=[{
                    'deletion':'pass'
                }]
            return Response(data)
        else:
            student.delete()
            data=[{
                    'deletion':'pass'
                }]
            return Response(data)
    else:
        data=[{
                'deletion':'fail'
            }]
        return Response(data)

@api_view(('GET',))
def mess(request):
    mess=Mess.objects.all()
    serializer=MessSerializer(mess,many=True)
    return Response(serializer.data)

@api_view(('GET','POST'))
def login(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        email=data[0]
        password=data[1]
        student=Student.objects.get(email=email)
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
        return Response()

@api_view(('GET','POST'))
def register(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        name=data[0]
        email=data[1]
        address=data[2]
        phone=data[3]
        password=data[4]
        Student.objects.create(
            name=name,
            email=email,
            address=address,
            phone=phone,
            password=password
        )
        data=[{
            'registered':'pass'
        }]
        return Response(data)
    else:
        return Response()

@api_view(('GET','POST'))
def studentUpdate(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        id=data[0]
        name=data[1]
        email=data[2]
        address=data[3]
        phone=data[4]
        room_no=data[5]
        hostel_fees=data[6]
        mess_fees=data[7]
        student=Student.objects.get(id=int(id))
        if student:
            student.name=name
            student.email=email
            student.address=address
            student.phone=phone
            if room_no=="None":
                if student.room:
                    room=Room.objects.get(number=student.room.number)
                    room.student=None
                    room.status="Empty"
                    student.room=None
                    room.save()
                    student.save()
            else:
                get_room=Room.objects.get(number=room_no)
                if get_room.status=="Occupied":
                    data=[{
                    'update':'fail',
                    'error': 'room'
                    }]
                    return Response(data)
                if student.room:
                    room=Room.objects.get(number=student.room.number)
                    room.student=None
                    room.status="Empty"
                    room.save()
                    new_room=Room.objects.get(number=int(room_no))
                    new_room.student=student
                    new_room.status="Occupied"
                    student.room=new_room
                    new_room.save()
                    student.save()
                else:
                    new_room=Room.objects.get(number=int(room_no))
                    new_room.student=student
                    new_room.status="Occupied"
                    student.room=new_room
                    new_room.save()
                    student.save()
            if hostel_fees=="Paid":
                student.hostel_fees=True
            else:
                student.hostel_fees=False
            if mess_fees=="Paid":
                student.mess_fees=True
            else:
                student.mess_fees=False
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
        return Response()

@api_view(('GET','POST'))
def hostelFees(request,id):
    if request.method=="POST":
        student=Student.objects.get(id=id)
        student.hostel_fees=True
        student.save()
        validate=[{
            'payment':'success'
        }]
        return Response(validate)
    else:
        return Response()

@api_view(('GET','POST'))
def messFees(request,id):
    if request.method=="POST":
        student=Student.objects.get(id=id)
        student.mess_fees=True
        student.save()
        validate=[{
            'payment':'success'
        }]
        return Response(validate)
    else:
        return Response()

@api_view(('GET','POST'))
def allotment(request):
    if request.method=="POST":
        data=list(request.data[0].values())
        id=data[0]
        name=data[1]
        email=data[2]
        address=data[3]
        student=Student.objects.get(id=id)
        if student:
            Allotment.objects.create(
                name=student.name,
                email=student.email,
                address=student.address,
                preference= 1 #Add here preference
            )
            data=[{
            'request':'pass'
            }]
            return Response(data)
        else:
            data=[{
            'request':'fail'
            }]
        return Response(data)
    else:
        return Response()