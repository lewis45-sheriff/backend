from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializer import ProfileSerializer, RegisterSerializer, CourseSerializer  # Consolidated imports
from base.models import Course, Profile 
from django.contrib.auth.models import User

# Custom Token Serializer to include additional information
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Profile retrieval for authenticated users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response({"status": "success", "data": serializer.data})

# Register new users
@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()  # Create the user
        
        # Create a profile for the user
        profile_data = {
            "bio": request.data.get("bio", ""),
            "location": request.data.get("location", ""),
            "birth_date": request.data.get("birth_date", None),
        }

        # Create and save the profile
        try:
            profile = Profile.objects.create(user=user, **profile_data)
            profile.save()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "status": "success",
            "message": "User registered successfully",
            "user": {
                "username": user.username,
                "email": user.email,
            },
            "profile": profile_data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Get courses for authenticated users

@api_view(['GET'])
def get_courses(request):
    """
    Retrieve a list of courses.
    """
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)