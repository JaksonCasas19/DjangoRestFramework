from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    #Serializa un campo para probar en nuestro API
    name = serializers.CharField(max_length=10)#Definir que solo reciba 10 caracteres