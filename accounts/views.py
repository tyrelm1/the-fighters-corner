from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')  
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
