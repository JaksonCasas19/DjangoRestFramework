from rest_framework import permissions

#Crear permisos personalizados

class UpdateOwnProfile(permissions.BasePermission):
    """ Permite usuario editar su propio perfil """

    def has_object_permission(self, request, view, obj):
        """ Chequear si usuario esta intentando editar su propio perfil """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

#Permite actualizar que el usuario actualize su propio perfil
class UpdateOwnStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile_id == request.user.id
