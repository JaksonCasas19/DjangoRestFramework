from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    #Clase Api View de prueba

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