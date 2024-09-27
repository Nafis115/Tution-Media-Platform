from rest_framework import serializers
from .models import TutorModel,TutorReview
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .constants import *


from rest_framework import serializers
from .models import User, TutorModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TutorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    user = UserSerializer(read_only=True)

    class Meta:
        model = TutorModel
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'email',
            'image',
            'gender',
            'phone_number',
            'designation',
            'education',
            'bio',
            'location',
            'subjects',
            'salary',
            'tutoring_experience',
            'medium_of_instruction',
        ]

 

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        
        if user_data:
            user = instance.user
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.email = user_data.get('email', user.email)
            user.save()

        instance.image = validated_data.get('image', instance.image)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.education=validated_data.get('education',instance.education)
        instance.location = validated_data.get('location', instance.location)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.tutoring_experience = validated_data.get('tutoring_experience', instance.tutoring_experience)
        instance.medium_of_instruction = validated_data.get('medium_of_instruction', instance.medium_of_instruction)
        instance.save()

        return instance



  





class TutorRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    image = serializers.ImageField(required=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, required=True)
    phone_number = serializers.CharField(max_length=15, required=True)
    location = serializers.CharField(max_length=100, required=True)
    subjects = serializers.CharField(max_length=100)
    education = serializers.CharField(max_length=50)
    salary = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, allow_null=True)
    tutoring_experience = serializers.CharField(max_length=20, required=True)
    medium_of_instruction = serializers.ChoiceField(choices=MEDIUM_OF_INSTRUCTION_CHOICES, required=True)
    designation = serializers.CharField(max_length=55, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password',
                  'image', 'gender', 'phone_number', 'education', 'designation', 'location', 'subjects', 
                  'salary', 'tutoring_experience', 'medium_of_instruction']

    def validate(self, data):
        # Validate password strength
        validate_password(data['password'])
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"error": "Passwords don't match"})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"error": "Email already exists"})
        return data

    def create(self, validated_data):
        user_data = {key: validated_data[key] for key in ['username', 'first_name', 'last_name', 'email', 'password']}
        user = User(**user_data)
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()

        tutor = TutorModel.objects.create(
            user=user,
            image=validated_data['image'],
            gender=validated_data['gender'],
            phone_number=validated_data['phone_number'],
            location=validated_data['location'],
            subjects=validated_data['subjects'],
            salary=validated_data.get('salary'),
            education=validated_data['education'],
            tutoring_experience=validated_data['tutoring_experience'],
            medium_of_instruction=validated_data['medium_of_instruction'],
            designation=validated_data['designation'],
        )


        return user



class TutorLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    new_password_confirm = serializers.CharField(required=True, write_only=True)
    
    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError({"new_password_confirm": "New passwords do not match."})
        return data

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.SerializerMethodField()

    class Meta:
        model = TutorReview
        fields = '__all__'
    
    def get_reviewer_name(self, obj):
        
        return obj.reviewer.user.username