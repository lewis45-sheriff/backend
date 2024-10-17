from django.urls import path
from .views import MyTokenObtainPairView, get_profile, register_user, get_courses
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('profile/', get_profile, name='get_profile'),  # Route to get user profile
    path('register/', register_user, name='register_user'),  # Route for user registration
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Route to obtain JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Route to refresh JWT token
    path('courses/' , get_courses, name='get_courses'),
]
