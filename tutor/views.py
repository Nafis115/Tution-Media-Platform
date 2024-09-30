from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import UpdateAPIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import TutorModel,TutorReview
from .serializers import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class TutorApiView(viewsets.ModelViewSet):
    queryset = TutorModel.objects.all()
    serializer_class = TutorSerializer

    def perform_create(self, serializer):
        serializer.save()

class TutorRegistrationApiView(APIView):
    serializer_class = TutorRegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            tutor = serializer.save()
            token = default_token_generator.make_token(tutor)
            uid = urlsafe_base64_encode(force_bytes(tutor.pk))
            
            confirm_link = f" https://tution-media-platform-backend.onrender.com/api/tutor/active/{uid}/{token}"
            email_subject = "Confirm Registration"
            email_body = render_to_string('register_email.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[tutor.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            
            return Response({"message": "Check your email for confirmation."}, status=201)  # Created status
            
        return Response(serializer.errors, status=400)  # Bad Request status


def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        tutor=User._default_manager.get(pk=uid)
        
    except(User.DoesNotExist):
        tutor=None
        
    if tutor is not None and default_token_generator.check_token(tutor,token):
        tutor.is_active=True 
        tutor.save()
        return redirect('https://tuitionmedia.netlify.app/login.html')
    else:
        return redirect('https://tuitionmedia.netlify.app/register')

class TutorLoginApiView(APIView):
    def post(self, request):
        serializer = TutorLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            tutor = authenticate(username=username, password=password)

            if tutor:
                try:
                    tutor_data = TutorModel.objects.get(user=tutor)
                    token, _ = Token.objects.get_or_create(user=tutor)
                    login(request, tutor)
                    return Response({'Token': token.key, 'tutor_id': tutor_data.id}, status=status.HTTP_200_OK)
                except TutorModel.DoesNotExist:
                    return Response({'error': "Tutor data not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorLogoutApiView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            if hasattr(request.user, 'auth_token'):
                request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        return Response({'message': 'You are not logged in.'}, status=status.HTTP_401_UNAUTHORIZED)

class ChangePasswordApiView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"detail": "Password updated successfully."}, status=status.HTTP_200_OK)



class TutorReviewViewset(viewsets.ModelViewSet):
    
    queryset = TutorReview.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tutor']