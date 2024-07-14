from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import StudentApiView,StudentRegistrationApiView,activate,StudentLoginApiView,StudentLogoutApiView,StudentUpdateAPIView,ChangePasswordApiView


router=DefaultRouter()

router.register('list',StudentApiView) 

urlpatterns = [
    path('',include(router.urls)),
    path("register/", StudentRegistrationApiView.as_view(), name="register"),
    path("login/", StudentLoginApiView.as_view(), name="login"),
    path('logout/',StudentLogoutApiView.as_view(),name='logout'),
    path('update_profile/',StudentUpdateAPIView.as_view(),name='update_profile'),
    path("active/<uid64>/<token>/",activate,name='activate'),
    path('change-password/<int:id>/', ChangePasswordApiView.as_view(), name='student-change-password'),
    
]
