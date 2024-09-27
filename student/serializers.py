from rest_framework import serializers
from .models import StudentModel
from django.contrib.auth.models import User
from tutor.constants import GENDER_CHOICES

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentModel
        fields = '__all__'
        

class StudentRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    image = serializers.ImageField(required=True)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, required=True)
    phone_number = serializers.CharField(max_length=15, required=True)
    location = serializers.CharField(max_length=100, required=True)
   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password','image', 'gender', 'phone_number', 'location']

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

        # Creating the  StudentModel
        student = StudentModel.objects.create(
            user=account,
            image=self.validated_data['image'],
            gender=self.validated_data['gender'],
            phone_number=self.validated_data['phone_number'],
            location=self.validated_data['location']
        )



        return account
class StudentLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)

           


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