from django.shortcuts import render
from . import tempData
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='/accounts/')
def home(request):
    policies = Policy.objects.all()
    context = {
        'policies': policies
    }
    return render(request, 'home.html', context)


@login_required(login_url='/accounts/')
def profile(request):
    context = {
        'profileData': tempData.profileData
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/accounts/')
def view_policies(request):

    context = {
        'all_policies': tempData.all_policies,
        'types': tempData.policyType,
        'a': [tempData.EC2_policies, tempData.S3_policies]
    }
    return render(request, 'view_policies.html', context)

   # return render(request, 'view_policies.html', {'types': tempData.policyType})


@login_required(login_url='/accounts/')
def my_policies(request):
    context = {

    }
    return render(request, 'my_policies.html', context)


@login_required(login_url='/accounts/')
def violations(request):
    context = {

    }
    return render(request, 'violations.html', context)


@login_required(login_url='/accounts/')
def login(request):
    context = {

    }
    return render(request, 'login.html', context)


@login_required(login_url='/accounts/')
def signup(request):
    context = {

    }
    return render(request, 'signup.html', context)


@login_required(login_url='/accounts/')
def logout(request):
    context = {

    }
    return render(request, 'home.html', context)
