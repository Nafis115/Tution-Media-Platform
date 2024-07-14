from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import (
    TutorApiView,
    TutorRegistrationApiView,
    activate,
    TutorLoginApiView,
    TutorLogoutApiView,
    ChangePasswordApiView,
    TutorFilterApiView,
    TutorEducationApiView,
    TutorReviewApiView,
    TutorDetailsUpdateApiView,
    TutorProfileUpdateAPIView
)


router=DefaultRouter()

router.register('list',TutorApiView) 

urlpatterns = [
    path('',include(router.urls)),
    path("register/", TutorRegistrationApiView.as_view(), name="tutor_register"),
    path("login/", TutorLoginApiView.as_view(), name="tutor_login"),
    path('logout/',TutorLogoutApiView.as_view(),name='logout'),
    path("active/<uid64>/<token>/",activate,name='activate'),
    path('education/', TutorEducationApiView.as_view(), name='tutor-education'),
    path('review/', TutorReviewApiView.as_view(), name='tutor-review'),
    path('update_profile/', TutorProfileUpdateAPIView.as_view(), name='update_profile'),
    path('filter', TutorFilterApiView.as_view(), name='tutor-list'),
    path('update_details/', TutorDetailsUpdateApiView.as_view(), name='tutor-update-profile'), 
    path('change-password/<int:id>/', ChangePasswordApiView.as_view(), name='tutor-change-password'),

    
    
]
