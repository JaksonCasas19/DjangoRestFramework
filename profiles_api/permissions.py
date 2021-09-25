from rest_framework import permissions

#Crear permisos personalizados


#Permite usuario editar su propio perfil
class UpdateOwnProfile(permissions.BasePermission):
    #Verificar si el usuario esta intentando editar su propio perfil
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        #Vamos a comparar si el obj es igual al request
        return obj.id == request.user.id