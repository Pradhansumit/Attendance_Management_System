from django.contrib import admin
from . import models


class AccountAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "is_admin", "is_staff"]


admin.site.register(models.Accounts, AccountAdmin)
admin.site.register(models.AttendanceSlot)

