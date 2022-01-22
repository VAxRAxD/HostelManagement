from . import views
from django.urls import path

urlpatterns=[
    path('students/',views.students,name="home"),
    path('rooms/',views.rooms,name="home"),
    path('mess/',views.mess,name="mess"),
    path('login/',views.login,name="login"),
    path('students/<str:id>/',views.studentDetails,name="student_details"),
    path('rooms/<str:id>/',views.roomDetails,name="room_details"),
    path('rooms/delete/<str:id>',views.deleteRoom,name="delete_room"),
    path('students/delete/<str:id>',views.deleteStudent,name="delete_student"),
    path('student/update/',views.studentUpdate,name="update_student"),
]