from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *

router=DefaultRouter()

router.register('list',StudentApiView)


urlpatterns = [
    path('',include(router.urls)),
    path("register/", StudentRegistrationApiView.as_view(), name="tutor_register"),
    path("login/", studentLoginApiView.as_view(), name="tutor_login"),
    path('logout/',StudentLogoutApiView.as_view(),name='logout'),
    path("active/<uid64>/<token>/",activate,name='activate'),
    path('change-password/', ChangePasswordApiView.as_view(), name='change-password'),

    
    
]