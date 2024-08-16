from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TuitionViewSet,ReviewViewset,TuitionDetail

router = DefaultRouter()
router.register('list', TuitionViewSet)
router.register('reviews', ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
     path("<int:pk>/", TuitionDetail.as_view(), name="tuition_detail"),
    
]


