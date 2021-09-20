from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Modelo base de datos para Usuario en el sistema"""
    email = models.EmailField(max_length=50,unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        #Obtener nombre completo del usuario
        return self.name

    def get_short_name(self):
        #Obtener nombre corto del usuario
        return self.name
    
    def __str__(self):
        #Retornar cadena representando nuestro usuario
        return self.email
