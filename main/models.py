from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from . import manager

STUDENT_DEPARTMENT = (
    ("BCA", "BCA"),
    ("MCA", "MCA"),
    ("MSC", "MSC"),
)


class Accounts(AbstractBaseUser):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)

    # blank=true for teacher which cannot be in a department
    department = models.CharField(
        max_length=12, blank=True, choices=STUDENT_DEPARTMENT, default="BCA")

    # blank=true for teacher which cannot be in a division
    division = models.CharField(max_length=12, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"

    objects = manager.CustomBaseManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class AttendanceSlot(models.Model):
    division = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    slot_id = models.IntegerField()
    unlocked = models.BooleanField(default = False)



class MarkedAttendance(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.PROTECT, related_name="ma_user")
    division = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    slot_id = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)