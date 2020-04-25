from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.http import HttpResponse


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

