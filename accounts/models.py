from django.db import models
from PIL import Image
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username=None
    email=models.CharField(_('email address'), unique=True, max_length=100)
    date_joined=models.DateTimeField(default=timezone.now)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission ? Return True"
        return True
    def is_staff_member(self):
        "Is the user a member of staff?"
        return self.is_staff
    @property
    def is_admin(self):
        "is the admin a member ?"
        return self.admin 
    def __str__(self):
        return self.email

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True, null=True)
    photo=models.ImageField(upload_to='users/%Y/%m/%d/', default='avatar.jpg')

    def __str__(self):
        return f'Profile of {self.user.username}'
    

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)



