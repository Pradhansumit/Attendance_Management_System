from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('teacher/', views.Teacher_dashboard, name="teacher_dashboard"),
    path('student/', views.Student_dashboard, name="student_dashboard"),
    path('admin-d/', views.Admin_dashboard, name="admin_dashboard"),
    path('logout/', views.logout_view, name="logout"),
    path('slot_creation/', views.slot_creation, name="slot_creation"),
    path('slot_deletion/', views.slot_deletion, name="slot_deletion"),
    path('mark-attendance/', views.mark_attendance, name="mark_attendance"),
]
