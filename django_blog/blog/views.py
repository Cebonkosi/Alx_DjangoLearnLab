from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login as auth_login

def register(request):
    """
    Handle user registration: show form, validate, create user and log them in.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in immediately
            auth_login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    """
    View and edit profile. If Profile model exists, use ProfileForm.
    """
    if request.method == 'POST':
        # If using Profile model
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')
    else:
        p_form = ProfileForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {
        'p_form': p_form
    })
