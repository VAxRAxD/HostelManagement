from . import views
from django.urls import path

urlpatterns=[
    path('students/',views.students,name="home"),
    path('rooms/',views.rooms,name="home"),
]