from rest_framework import generics,viewsets
from .models import Tuition
from .serializers import TuitionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TuitionFilter


class TuitionViewSet(viewsets.ModelViewSet):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer

class TuitionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer



class TuitionFilterApiView(generics.ListAPIView):
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TuitionFilter