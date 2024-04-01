from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    costom user model manager where email is the unique identifiers for authentication instead of username.
    """

    def create_user(self,email,password,**extra_fields):
        """
        create and save a user with the given email and password,
        """
        if not email:
            raise ValueError('Users must have an email address')
        # check whether email has already been used
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # set_password() method will take care of password encryptiond
        user.save()  # call save() to create and save thedf user instance
        return user
    
    def crate_superuser(self, email, password, **extra_fields):
        """
        create and save a superuser with the given email and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_supseruser',True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
