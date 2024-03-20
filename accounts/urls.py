from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import signup_view

urlpatterns = [
    path('accounts/signup/', signup_view, name='account_signup'),  # Custom signup view
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),  # Django login view
    path('accounts/logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # Django logout view
]
