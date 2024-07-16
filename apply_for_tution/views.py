# views.py
from .models import Application
from .serializers import ApplicationSerializer
from tutor.models import TutorModel  
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ApplicationCreateView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class =  ApplicationSerializer
    
  
    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.query_params)
        tutor_id = self.request.query_params.get('tutor_id')
        if tutor_id:
            queryset = queryset.filter(tutor_id=tutor_id)
        return queryset

