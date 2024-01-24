from django.conf import settings
from django.db import models
from django.contrib.auth.models import Permission, Group

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.dispatch import receiver
from django.forms import ValidationError
from djmoney.models.fields import MoneyField
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.utils.timezone import now
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save



class UserAccountManager(BaseUserManager):
    def create_user(self , last_name, name, email,password=None):
        if not email or len(email) <= 0 : 
            raise  ValueError("Email field is required !")
        
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            last_name=last_name, name=name, email=email
            
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_founder(self , last_name, name, email ,password=None):
        user=self.create_user(last_name, name, email, password)
        user.is_founder=True
        user.save(using = self._db)
        return user
    
        

    def create_superuser(self , last_name, name, email,password=None):
        user = self.create_user( last_name, name, email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save(using = self._db)
        return user
    def create_investor(self , last_name, name, email ,password=None):
        user=self.create_user(last_name, name, email, password)
        user.is_founder=False
        user.save(using = self._db)
        return user
      
class UserAccount(AbstractBaseUser):
          
    email = models.EmailField(max_length = 200 , unique = True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
      
    is_founder = models.BooleanField(default = False)
    has_subscription = models.BooleanField(default=False)

      
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "last_name"]
      
    # defining the manager for the UserAccount model
    objects = UserAccountManager()
      
    def __str__(self):
        return str(self.email)
      
    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True





