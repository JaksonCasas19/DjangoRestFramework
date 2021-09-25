from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializer, models, permissions
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class HelloApiView(APIView):
    #Clase Api View de prueba
    serializer_class = serializer.HelloSerializer

    def get(self,request,format=None):
        #Retornar lista de caracteristicas del APIView
        an_apiview = [
            'Usamos metodos HTTP como funciones (get,post,patch,put,delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manuealmente a los URLs',
        ]
        #Para convertir la información en formato JSON  debe ser una lista o un diccionario
        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
        #Crea un mensaje con nuestro nombre

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        # Put: Maneja actualizar un objecto. El pk indicar que objeto se va actualizar
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        #Maneja actualizacion parcial de un objeto
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        #Elimina un objeto
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    #Api de tes viewset

    #Se invoca al serializar para realizar operaciones(CRUD)
    serializer_class = serializer.HelloSerializer

    def list(self,request):
    #Retornar mensaje de Hola Mundo
        a_viewset = [
            'Usa accion (list,create,retrive,update,partial_update',
            'Automaticamente mapea a lso URLs usando routers',
            'Provee mas funcionalidad con menos codigo'
        ]
        return Response({'message':'Hola!','a_viewset':a_viewset})
    
    def create(self,request):
        #Crear datos, para crear un mensaje hola mundo
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola{name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request,pk=None):
        #Obtiene un objeto y su ID
        return Response({'http_method':'GET'})
    
    def update(self, request,pk=None):
        #Actualiza un objeto
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request,pk=None):
        #Actualiza parcialmente el objeto
        return Response({'http_method':'PATCH'})

    def destroy(self, request,pk=None):
        #Destruye un objeto
        return Response({'http_method':'DELETE'})


#Crear y actualizar perfiles
class UserProfileViewSet(viewsets.ModelViewSet):

     serializer_class = serializer.UserProfileSerializer #Llamar desde el serializador
     queryset = models.UserProfile.objects.all()
     authentication_classes = (TokenAuthentication)