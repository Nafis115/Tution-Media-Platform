from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TuitionViewSet,TuitionDetailAPIView,TuitionFilterApiView

router = DefaultRouter()
router.register('list', TuitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tuitions/<int:pk>/',TuitionDetailAPIView.as_view(), name='tuition-detail'),
     path('filter/', TuitionFilterApiView.as_view(), name='tuition-filter'),
]


