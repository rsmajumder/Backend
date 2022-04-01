from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone','first_name', 'last_name')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'password' ,'first_name', 'last_name' )
        

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],phone=validated_data['phone'],password=validated_data['password'],first_name=validated_data['first_name'],last_name=validated_data['last_name'] )

        return user



#Change Password  Serializer
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


#UserProfile Serializer
class userProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = userProfile
		fields ='__all__'

#OTP Serializer
class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('number',)


#OTP check Serializer
class OTPCheckserializer(serializers.Serializer):
    otp = serializers.CharField(max_length=128, write_only=True)

