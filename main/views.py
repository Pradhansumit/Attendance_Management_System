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


def Admin_dashboard(request):
    return render(request, 'main/admin-dashboard.html', locals())


def Teacher_dashboard(request):
    return render(request, 'main/teacher-dashboard.html', locals())


def Student_dashboard(request):
    # print(request.username)
    # user = models.Accounts.objects.get(phone_number=request.user)
    return render(request, 'main/student-dashboard.html', locals())
