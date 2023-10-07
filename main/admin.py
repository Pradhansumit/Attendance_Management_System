from django.contrib import admin
from . import models


class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "is_admin", "is_staff"]

class AttendanceSlotAdmin(admin.ModelAdmin):
    list_display = ["id", "department", "division", "slot_id", "unlocked"]


class MarkAttendanceAdmin(admin.ModelAdmin):
    list_display = ["id", "user","department", "division", "slot_id","date_time"]

admin.site.register(models.Accounts, AccountAdmin)
admin.site.register(models.AttendanceSlot, AttendanceSlotAdmin)
admin.site.register(models.MarkedAttendance, MarkAttendanceAdmin)

