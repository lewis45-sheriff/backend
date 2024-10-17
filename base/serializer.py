from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from .models import Course
# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'email']  # User-specific fields

# Serializer for Profile model
class ProfileSerializer(serializers.ModelSerializer):
    # Include UserSerializer to access the related user's details
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'location', 'birth_date', 'avatar', 'role']  # Profile-specific fields

# Serializer for handling user registration
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is not read back in responses
        }

    def create(self, validated_data):
        # Use Django's create_user method to handle password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor', 'duration', 'price']  # Add relevant fields