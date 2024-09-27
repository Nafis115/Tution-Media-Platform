from rest_framework import viewsets
from .models import Tuition,Review
from .serializers import TuitionSerializer,ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TuitionViewSet(viewsets.ModelViewSet):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']



class ReviewViewset(viewsets.ModelViewSet):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    