# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    bio = request.data.get('bio', '')  # Optional
    location = request.data.get('location', '')  # Optional
    birth_date = request.data.get('birth_date', None)  # Optional

    if User.objects.filter(username=username).exists():
        return Response({'detail': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    Profile.objects.create(user=user, bio=bio, location=location, birth_date=birth_date)

    return Response({'detail': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
