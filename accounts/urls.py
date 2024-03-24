from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import signup_view

urlpatterns = [
    path('accounts/signup/', signup_view, name='account_signup'), 
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]