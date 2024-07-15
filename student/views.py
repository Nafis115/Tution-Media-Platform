# rest framework modules
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
# registration and login modules
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect

#modules of project
from .models import StudentModel
from .serializers import StudentSerializer,StudentRegistrationSerializer,StudentLoginSerializer,StudentUpdateSerializer,ChangePasswordSerializer
from django.contrib.auth.models import User

#for sending email modules
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

# student list api
class StudentApiView(viewsets.ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    
    
# student registration view


class StudentRegistrationApiView(APIView):
    serializer_class=StudentRegistrationSerializer
    
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data) #user details stor in serializer
        
        if serializer.is_valid(): 
            student=serializer.save() # save serializer in database
            token=default_token_generator.make_token(student)  #generate token of student
            uid=urlsafe_base64_encode(force_bytes(student.pk)) #more specified the confirmation link
            
            confirm_link=f"https://tution-media-platform.onrender.com/api/student/active/{uid}/{token}" #link send for confirm
            email_subject="Confirm Registration"
            email_body=render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[student.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            
            return Response("Check email for confirmation")
        return Response(serializer.errors)
    
# activate view when user click the link
 
def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        student=User._default_manager.get(pk=uid)
        
    except(User.DoesNotExist):
        student=None
        
    if student is not None and default_token_generator.check_token(student,token):
        student.is_active=True # account active
        student.save()
        return redirect('login')
    else:
        return redirect('register')
    
            
# student login view   
            
class StudentLoginApiView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=self.request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
           
            student = authenticate(username=username, password=password)
            
            if student:
                try:
                  
                    student_data = StudentModel.objects.get(user=student)
                    student_id = student_data.id
                    
                    token, _ = Token.objects.get_or_create(user=student)
                    login(request, student) 
                    
                    return Response({'Token': token.key, 'student_id': student_id})
                except StudentModel.DoesNotExist:
                    return Response({'error': "Student data not found"})
            else:
                return Response({'error': "Invalid credentials"})
        return Response(serializer.errors)
        
# student logout view
               
class StudentLogoutApiView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            if hasattr(request.user, 'auth_token'):
                request.user.auth_token.delete()
            logout(request)
            return redirect('login')
        else:
            return Response({'message': 'You are not logged in.'}, status=status.HTTP_401_UNAUTHORIZED)
    



class StudentUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentUpdateSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
    

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