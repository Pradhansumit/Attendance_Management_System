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
            attendance_slot = models.AttendanceSlot.objects.all()[0]
            # print(user, "is not valid")
            if user is not None:
                login(request, user)
                if login:
                    if user.is_staff and not user.is_admin: 
                        return redirect('teacher_dashboard')
                    elif user.is_staff and user.is_admin: 
                        return redirect('admin_dashboard')
                    else:
                        if attendance_slot:
                            attn_div = attendance_slot.division
                            attn_dept = attendance_slot.department
                            user_div = request.user.division
                            user_dept = request.user.department
                            print("attn_div", attn_div, "attn_dept", attn_dept,"user_div", user_div,"user_dept",user_dept)
                            #print("Student can enter")
                            #print(request.user.department)
                            if attn_div == user_div and attn_dept == user_dept:
                                return redirect("student_dashboard")
                            else:
                                return render(request, "main/blank.html")
                        else:
                            raise ValueError("Attendance is locked")

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
    print(user)
    attendance = models.AttendanceSlot.objects.all()[0]
    #print(attendance.slot_id)
    return render(request, 'main/student-dashboard.html', locals())


# to create a new slot for attendance
def slot_creation(request):
    if not models.AttendanceSlot.objects.all():
        if request.method == "GET":
            slot_id = request.GET['slot_id']
            division_data = request.GET['division_data']
            print("slot data",slot_id,"division data",division_data)
            #print("type of division_data", type(division_data))
            
            if division_data == "1":
                print("-------------")
                print("Value ara")
                print("-------------")
                department = "BCA"
                division = "A"
                model = models.AttendanceSlot(department=department,division=division, slot_id=slot_id, unlocked=True)
                model.save()
                
            elif division_data == "2": 
                department = "BCA"
                division = "B"
                model.objects.create(department=department,division = division, slot_id = slot_id, unlocked= True)
                
            elif division_data == "3": 
                department = "BCA"
                division = "C"
                model.objects.create(department=department,division = division, slot_id = slot_id, unlocked= True)

            elif division_data == "4":
                department = "MCA"
                division = "A"
                model.objects.create(department=department,division = division, slot_id = slot_id, unlocked= True)
            
            elif division_data == "5":
                department = "MCA"
                division = "B"
                model.objects.create(department=department,division = division, slot_id = slot_id, unlocked= True)

            data ={
                "message" : "created"
            }
            return JsonResponse(data)


# to delete existing slot for attendance
def slot_deletion(request):
    if request.method == "GET":
        slot_id = request.GET['slot_id']
        model = models.AttendanceSlot.objects.filter(slot_id = slot_id)
        #print("model", model)

        if model:
            print("-----")
            print("slot chlu h baba")
            print("-----")
            model.delete() #delete the slot
            
            data ={
                "message" : "deleted"
            }
            return JsonResponse(data)

        

