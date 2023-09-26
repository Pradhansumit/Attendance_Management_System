from django.contrib.auth.models import BaseUserManager


class CustomBaseManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Phone Number is required")

        user = self.model(phone_number=phone_number)

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Phone Number is required")

        user = self.model(phone_number=phone_number)

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self.db)
        return user
