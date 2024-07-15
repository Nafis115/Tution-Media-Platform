# rest framework modules
from rest_framework import viewsets,generics,status,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.authentication import TokenAuthentication
# registration and login modules
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect

#modules of project
from .models import TutorModel,TutorEducation,TutorReview
from .serializers import (
    TutorSerializer,TutorRegistrationSerializer,TutorLoginSerializer,TutorDetailsSerializer,TutorEducationSerializer,TutorReviewSerializer,ChangePasswordSerializer,TutorUpdateSerializer)

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import Http404
from .filters import TutorFilter
#for sending email modules
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

# Tutor list api
class TutorApiView(viewsets.ModelViewSet):
    queryset=TutorModel.objects.all()
    serializer_class=TutorSerializer
    
    
# Tutor registration view


class TutorRegistrationApiView(APIView):
    serializer_class=TutorRegistrationSerializer
    
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data) #user details stor in serializer
        
        if serializer.is_valid(): 
            tutor=serializer.save() # save serializer in database
            token=default_token_generator.make_token(tutor)  #generate token of tutor
            uid=urlsafe_base64_encode(force_bytes(tutor.pk)) #more specified the confirmation link
            
            confirm_link=f"http://127.0.0.1:8000/tutor/active/{uid}/{token}" #link send for confirm
            email_subject="Confirm Registration"
            email_body=render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[tutor.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            
            return Response("Check email for confirmation")
        return Response(serializer.errors)
    
# activate view when user click the link
 
def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        tutor=User._default_manager.get(pk=uid)
        
    except(User.DoesNotExist):
        tutor=None
        
    if tutor is not None and default_token_generator.check_token(tutor,token):
        tutor.is_active=True # account active
        tutor.save()
        return redirect('tutor_login')
    else:
        return redirect('tutor_register')
    
            
# tutor login view   
            
class TutorLoginApiView(APIView):
    def post(self, request):
        serializer = TutorLoginSerializer(data=self.request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            # Check if Tutor exists in our database
            tutor = authenticate(username=username, password=password)
            
            if tutor:
                try:
                    # Get the tutor_id from the Tutor model
                    tutor_data = TutorModel.objects.get(user=tutor)
                    tutor_id = tutor_data.id
                    
                    token, _ = Token.objects.get_or_create(user=tutor)
                    login(request, tutor)  # Log in the tutor
                    
                    return Response({'Token': token.key, 'tutor_id': tutor_id})
                except TutorModel.DoesNotExist:
                    return Response({'error': "Tutor data not found"})
            else:
                return Response({'error': "Invalid credentials"})
        return Response(serializer.errors)
    
    
class TutorProfileUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TutorUpdateSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
        
# tutor logout view
               
class TutorLogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
    




#tutor detail update view
class TutorDetailsUpdateApiView(generics.UpdateAPIView):
    
    serializer_class = TutorDetailsSerializer
    permission_classes = [IsAuthenticated]  
    def get_object(self):
        try:
            return TutorModel.objects.get(user=self.request.user)
        except TutorModel.DoesNotExist:
            raise Http404("Tutor details not found for the user")

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



#tutor educational view      
class TutorEducationApiView(generics.CreateAPIView):
    queryset=TutorEducation.objects.all()
    serializer_class=TutorEducationSerializer
    
    def perform_create(self, serializer):
        tutor=TutorModel.objects.get(user=self.request.user)
        serializer.save(tutor=tutor)

#tutor review
class TutorReviewApiView(generics.CreateAPIView):
    queryset=TutorReview.objects.all()
    serializer_class=TutorReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)
        
        
#for filter view


class TutorFilterApiView(generics.ListAPIView):  # Marked view class name
    queryset = TutorModel.objects.all()  # Marked model name
    serializer_class = TutorDetailsSerializer  # Marked serializer class name
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TutorFilter  # Marked filter class name
    search_fields = ['preferred_area_to_teach']
    ordering_fields = ['preferred_area_to_teach', 'preferred_class', 'preferred_subjects']

    

    

class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)