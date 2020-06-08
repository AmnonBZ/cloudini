from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserUpdateForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
            return HttpResponse("<h1>Thanks for registering, Cloudinis's team will contact you soon</h1>")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    context = {
        'myuser' : request.user,
    }

    return render(request, 'registration/profile.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid() :
            user_form.save()
            messages.success(request, f'Your account has been updated successfully !')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'form': user_form,
        'myuser' : request.user,
    }

    return render(request, 'registration/update_profile.html', context)

