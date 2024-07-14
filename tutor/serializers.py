from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import *


class TutorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=TutorModel
        fields='__all__'

class TutorRegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)

    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']
        
    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']

        #checking password for both same
        if password!=confirm_password:
            raise serializers.ValidationError({'error' : "Password Doesn't Matched"}) #raising error

        #checking email that exist or not

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"}) #raised error

        #creating account of Tutor
        account=User(username=username,first_name=first_name,last_name=last_name,email=email)
        #set password for the account
        account.set_password(password)
        #we set account active default false because we cross check the user and then active
        account.is_active=False
        account.save()
        
        tutor = TutorModel.objects.create(user=account)
        return account

class TutorLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)

class TutorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

class TutorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorModel
        fields = '__all__' 
        
class TutorEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=TutorEducation
        fields=['Exam_Name', 'passing_year', 'institution', 'Group', 'grade']    

class TutorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorReview
        fields = ['tutor', 'reviewer', 'rating', 'comment']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

    def validate(self, attrs):
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError("New password cannot be the same as the old password")
        return attrs