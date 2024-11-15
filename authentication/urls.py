from django.urls import path
from .views import ForgotPasswordView, ResetPasswordView, SignUpView, LoginView, UserDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('password/forgot/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('password/reset/<str:token>/', ResetPasswordView.as_view(), name='reset-password'),
]
