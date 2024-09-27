from rest_framework import viewsets
from .models import ContactSubmission
from .serializers import ContactSubmissionSerializer

class ContactSubmissionViewSet(viewsets.ModelViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer