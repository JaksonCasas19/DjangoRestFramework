from django.urls import path
from profiles_api import views

# .as_view -> No podemos ver una clase se de cargar como funcion 

urlpatterns = [
    path('hello-view',views.HelloApiView.as_view()),
]
