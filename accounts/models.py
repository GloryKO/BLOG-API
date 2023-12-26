from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('user must have an email')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        """create and return a super user """
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractUser):
    name = models.CharField(null=True,blank=True,max_length=100)
    email= models.EmailField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects=UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []