from django.contrib.auth.models import User
from nuser.models import UserProfile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password', 'first_name', 'email')

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields=('activation_key','key_expires')