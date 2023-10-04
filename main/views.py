from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import models
from . import forms

# view to display the homepage...


def Index(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            # to check the whether the form is valid or not
            # print("REQUEST IS VALID | FORM IS VALID")
            phone_number = request.POST["phone_number"]
            password = request.POST["password"]
            # check the password value coming is as given or not
            # print(phone_number, password)
            user = authenticate(
                request, phone_number=phone_number, password=password)
            # to check the whether the user is returning any object or is None
            # print(user, "is not valid")
            if user is not None:
                login(request, user)
                if login:
                    if user.is_staff:
                        return redirect('teacher_dashboard')
                    elif user.is_admin:
                        return redirect('admin_dashboard')
                    else:
                        return redirect("student_dashboard")

        else:
            raise ValueError("Enter correct credentials")

    else:
        form = forms.LoginForm()
        return render(request, "main/index.html", locals())


def logout_view(request):
    logout(request)
    return redirect('home')


def Admin_dashboard(request):
    return render(request, 'main/admin-dashboard.html', locals())


def Teacher_dashboard(request):
    return render(request, 'main/teacher-dashboard.html', locals())


def Student_dashboard(request):
    user = request.user
    return render(request, 'main/student-dashboard.html', locals())


def slot_creation(request):
    if request.method == "GET":
        slot_id = request.GET['slot_id']
        division_data = request.GET['division_data']
        print(slot_id,division_data)
        model = models.AttendanceSlot.objects
        
        if division_data == 1:
            department = "BCA"
            division = "A"
            model.create(department=department,division = division, slot_id = slot_id, unlocked= True)
            
        elif division_data == 2: 
            department = "BCA"
            division = "B"
            model.create(department=department,division = division, slot_id = slot_id, unlocked= True)
            
        elif division_data == 3: 
            department = "BCA"
            division = "C"
            model.create(department=department,division = division, slot_id = slot_id, unlocked= True)

        elif division_data == 4:
            department = "MCA"
            division = "A"
            model.create(department=department,division = division, slot_id = slot_id, unlocked= True)
        
        elif division_data == 5:
            department = "MCA"
            division = "B"
            model.create(department=department,division = division, slot_id = slot_id, unlocked= True)

        data ={
            "message" : "created"
        }
        return JsonResponse(data)

def slot_deletion(request):
    if request.method == "GET":
        slot_id = request.GET['slot_id']
        division_data = request.GET['division_data']