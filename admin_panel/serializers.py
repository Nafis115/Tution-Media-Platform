from .models import AdminModel
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
# serializers makings
#user serializer represent a Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']



class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AdminModel
        fields = ['id', 'mobile_no', 'user']
        

#registration serializer

class AdminRegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    mobile_no=serializers.CharField(max_length=12)
    
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','mobile_no','password','confirm_password']
        
    def save(self):
        username=self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email=self.validated_data['email']
        mobile_no=self.validated_data['mobile_no']
        password=self.validated_data['password']
        confirm_password=self.validated_data['confirm_password']

        #checking password for both same
        if password!=confirm_password:
  
            raise serializers.ValidationError({'error' : "Password Doesn't Matched"}) #raising error

        #checking email that exist or not

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"}) #raised error

        #creating account of Admin
        account=User(username=username,first_name=first_name,last_name=last_name,email=email)
        #set password for the account
        account.set_password(password)
        #we set account active default false because we cross check the user and then active
        account.is_active=False
        account.save()
        
        admin = AdminModel.objects.create(user=account, mobile_no=mobile_no)
        return account

class AdminLoginSerializer(serializers.Serializer):
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