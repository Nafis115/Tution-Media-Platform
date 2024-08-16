# views.py
from .models import Application
from .serializers import ApplicationSerializer
from tutor.models import TutorModel  
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tuition','tutor']

