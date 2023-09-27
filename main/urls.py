from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('teacher/', views.Teacher_dashboard, name="teacher_dashboard"),
    path('student/', views.Student_dashboard, name="student_dashboard"),
    path('admin/', views.Admin_dashboard, name="admin_dashboard"),
]
