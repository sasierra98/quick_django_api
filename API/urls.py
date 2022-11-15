from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from API.views import UserView, UserDetailView, RegisterView

urlpatterns = [
    path('user', UserView.as_view()),
    path('user/signup', RegisterView.as_view()),
    path('user/login', jwt_views.TokenObtainPairView.as_view()),
    path('user/login/refresh', jwt_views.TokenRefreshView.as_view()),
    path('user/<int:user_id>', UserDetailView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
