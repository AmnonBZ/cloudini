from django.shortcuts import render
from . import tempData


def home(request):
    context = {
        'policies': tempData.policies
    }
    return render(request, 'home.html', context)


def profile(request):
    context = {
        'profileData': tempData.profileData
    }
    return render(request, 'profile.html', context)


def view_policies(request):

    context = {
        'all_policies': tempData.all_policies,
        'types': tempData.policyType,
        'a': [tempData.EC2_policies, tempData.S3_policies]
    }
    return render(request, 'view_policies.html', context)

   # return render(request, 'view_policies.html', {'types': tempData.policyType})


def my_policies(request):
    context = {

    }
    return render(request, 'my_policies.html', context)


def violations(request):
    context = {

    }
    return render(request, 'violations.html', context)


def login(request):
    context = {

    }
    return render(request, 'login.html', context)


def signup(request):
    context = {

    }
    return render(request, 'signup.html', context)


def logout(request):
    context = {

    }
    return render(request, 'home.html', context)
