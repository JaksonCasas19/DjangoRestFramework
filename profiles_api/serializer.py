from django.db.models import fields
from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    #Serializa un campo para probar en nuestro API
    name = serializers.CharField(max_length=10)#Definir que solo reciba 10 caracteres

class UserProfileSerializer(serializers.ModelSerializer):
    #Serializa objeto de perfil de usuario
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    
    def create(self, validated_data):
        #Crear y retornar nuevo usuario
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user