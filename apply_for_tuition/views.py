from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Application
from .serializers import ApplicationSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tuition', 'tutor']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        previous_status = instance.status

        response = super().update(request, *args, **kwargs)
        instance.refresh_from_db()

        if instance.status == 'accepted' and previous_status != 'accepted':
            email_subject = "Your Tuition Application Accepted"
            email_body = render_to_string('admin_email.html', {'user': instance.tutor.user, 'tuition': instance.tuition})
            
            email = EmailMultiAlternatives(email_subject, '', to=[instance.tutor.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

        return response
