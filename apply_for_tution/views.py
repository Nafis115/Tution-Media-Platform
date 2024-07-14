# views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import IsTutor  
from tutor.models import TutorModel  
from django.shortcuts import get_object_or_404

class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsTutor]  # Apply the custom permission class here

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Assuming you retrieve the logged-in tutor and attach it to the application
            tutor_instance = get_object_or_404(TutorModel, user=request.user)  # Adjust based on your actual model structure
            serializer.save(tutor=tutor_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsTutor]  # Apply the custom permission class here

    def get_queryset(self):
        # Assuming you retrieve applications where the tutor is the logged-in user
        tutor_instance = get_object_or_404(TutorModel, user=self.request.user)  # Adjust based on your actual model structure
        return Application.objects.filter(tutor=tutor_instance)
