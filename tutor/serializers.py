from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TutorModel
        fields = '__all__'

class TutorRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    image = serializers.ImageField(required=True)
    gender = serializers.CharField(max_length=1, required=True)
    phone_number = serializers.CharField(max_length=15, required=True)
    location = serializers.CharField(max_length=100, required=True)
    tuition_district = serializers.CharField(max_length=100, required=True)
    minimum_salary = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, allow_null=True)
    status = serializers.CharField(max_length=20, required=False, allow_blank=True)
    days_per_week = serializers.IntegerField(default=5)
    tutoring_experience = serializers.CharField(max_length=20, required=True)
    extra_facilities = serializers.CharField(max_length=200, required=False, allow_blank=True)
    medium_of_instruction = serializers.CharField(max_length=20, required=True)
   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password',
                  'image', 'gender', 'phone_number', 'location', 'tuition_district', 'minimum_salary',
                  'status', 'days_per_week', 'tutoring_experience', 'extra_facilities',
                  'medium_of_instruction']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        # Checking password match
        if password != confirm_password:
            raise serializers.ValidationError({'error': "Password Doesn't Match"})

        # Checking if email exists
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email Already Exists"})

        # Creating the User account
        account = User(username=username, first_name=first_name, last_name=last_name, email=email)
        account.set_password(password)
        account.is_active = False  # User needs verification
        account.save()

        # Creating the associated TutorModel
        tutor = TutorModel.objects.create(
            user=account,
            image=self.validated_data['image'],
            gender=self.validated_data['gender'],
            phone_number=self.validated_data['phone_number'],
            location=self.validated_data['location'],
            tuition_district=self.validated_data['tuition_district'],
            minimum_salary=self.validated_data.get('minimum_salary'),
            status=self.validated_data.get('status', 'Available'),
            tutoring_experience=self.validated_data['tutoring_experience'],
            extra_facilities=self.validated_data.get('extra_facilities', ''),
            medium_of_instruction=self.validated_data['medium_of_instruction'],
           
        )



        return account
class TutorLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)

        
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