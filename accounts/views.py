from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Handle login logic if needed
            return redirect('home')  # Redirect to home page upon successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
