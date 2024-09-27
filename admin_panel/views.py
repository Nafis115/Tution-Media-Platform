# rest framework modules
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# registration and login modules
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
#modules of project
from .models import AdminModel
from .serializers import AdminSerializer,AdminRegistrationSerializer,AdminLoginSerializer,ChangePasswordSerializer
from django.contrib.auth.models import User

#for sending email modules
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

# Admin list api
class AdminApiView(viewsets.ModelViewSet):
    queryset=AdminModel.objects.all()
    serializer_class=AdminSerializer
    
    
# Admin registration view


class AdminRegistrationApiView(APIView):
    serializer_class=AdminRegistrationSerializer
    
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data) #user details stor in serializer
        
        if serializer.is_valid(): 
            admin=serializer.save() # save serializer in database
            token=default_token_generator.make_token(admin)  #generate token of admin
            uid=urlsafe_base64_encode(force_bytes(admin.pk)) #more specified the confirmation link
            
            confirm_link=f"https://tution-media-platform.onrender.com/api/admin/active/{uid}/{token}" #link send for confirm
            email_subject="Confirm Registration"
            email_body=render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[admin.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            
            return Response("Check email for confirmation")
        return Response(serializer.errors)
    
# activate view when user click the link
 
def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        admin=User._default_manager.get(pk=uid)
        
    except(User.DoesNotExist):
        admin=None
        
    if admin is not None and default_token_generator.check_token(admin,token):
        admin.is_active=True # account active
        admin.save()
        return redirect('login')
    else:
        return redirect('register')
    
            
# admin login view   
            
class AdminLoginApiView(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=self.request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
           
            admin = authenticate(username=username, password=password)
            
            if admin:
                try:
                  
                    admin_data = AdminModel.objects.get(user=admin)
                    admin_id = admin_data.id
                    
                    token, _ = Token.objects.get_or_create(user=admin)
                    login(request, admin) 
                    
                    return Response({'Token': token.key, 'admin_id': admin_id})
                except AdminModel.DoesNotExist:
                    return Response({'error': "admin data not found"})
            else:
                return Response({'error': "Invalid credentials"})
        return Response(serializer.errors)
        
# admin logout view
               
class AdminLogoutApiView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            if hasattr(request.user, 'auth_token'):
                request.user.auth_token.delete()
            logout(request)
            return redirect('login')
        else:
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

