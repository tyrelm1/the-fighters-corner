from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    # Add any additional fields if needed
    class Meta(UserCreationForm.Meta):
        # Define fields if needed
        fields = ('username', 'email')

class CustomAuthenticationForm(AuthenticationForm):
    # Add any additional fields if needed
    remember_me = forms.BooleanField(required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
