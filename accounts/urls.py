from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import signup_view

urlpatterns = [
    path('accounts/', PostCreateView.as_view(template_name='signup.html'), name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', signup_view, name='signup'),
]