from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *

router=DefaultRouter()

router.register('list',TutorApiView) 

urlpatterns = [
    path('',include(router.urls)),
    path("register/", TutorRegistrationApiView.as_view(), name="tutor_register"),
    path("login/", TutorLoginApiView.as_view(), name="tutor_login"),
    path('logout/',TutorLogoutApiView.as_view(),name='logout'),
    path("active/<uid64>/<token>/",activate,name='activate'),
    path('change-password/<int:id>/', ChangePasswordApiView.as_view(), name='tutor-change-password'),

    
    
]
