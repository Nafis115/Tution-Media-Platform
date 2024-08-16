from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AdminApiView,AdminRegistrationApiView,activate,AdminLoginApiView,AdminLogoutApiView


router=DefaultRouter()

router.register('list',AdminApiView) 

urlpatterns = [
    path('',include(router.urls)),
    path("register/", AdminRegistrationApiView.as_view(), name="register"),
    path("login/", AdminLoginApiView.as_view(), name="login"),
    path('logout/',AdminLogoutApiView.as_view(),name='logout'),
    path("active/<uid64>/<token>/",activate,name='activate'),
    
    
]
