from django.db import router
from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


# .as_view -> No podemos ver una clase se de cargar como funcion 

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')

urlpatterns = [
    path('hello-view',views.HelloApiView.as_view()),
    path('',include(router.urls))
]
