from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactSubmissionViewSet


router = DefaultRouter()
router.register("list", ContactSubmissionViewSet,)


urlpatterns = [
    path('', include(router.urls)),
]