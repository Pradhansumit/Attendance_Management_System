from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('teacher/', views.Teacher_dashboard, name="teacher_dashboard"),
    path('student/', views.Student_dashboard, name="student_dashboard"),
    path('admin-d/', views.Admin_dashboard, name="admin_dashboard"),
    path('admin-t/', views.Admin_dashboard_teacher, name="admin_dashboard_teacher"),
    path('admin-s/', views.Admin_dashboard_student, name="admin_dashboard_student"),
    path('admin-r/', views.Admin_dashboard_register, name="admin_dashboard_register"),
    path('logout/', views.logout_view, name="logout"),
    path('slot_creation/', views.slot_creation, name="slot_creation"),
    path('slot_deletion/', views.slot_deletion, name="slot_deletion"),
    path('mark-attendance/', views.mark_attendance, name="mark_attendance"),
    path('check_slot/', views.check_slot, name="check_slot"),
    path('<int:id>/', views.Profile, name="profile"),
    
]
