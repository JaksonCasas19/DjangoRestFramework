from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    #Manager para perfiles de usuario
    def create_user(self,email,name,password=None):
        #Crear Nuevo usuario profile
        if not email:
            raise ValueError('Usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user

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

class ProfileFeedItem(models.Model):
    #Perfil de Status Update
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text

