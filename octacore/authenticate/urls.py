from django.urls import path,include
from django.views.generic import TemplateView
from authenticate.views import UserRegistrationView,UserLoginView,EntireUserProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', EntireUserProfileView, name='profile')
]