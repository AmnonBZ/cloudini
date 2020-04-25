from django.shortcuts import render
from . import tempData
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect


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
def create_a_policy_page(request):
    context = {
        'policies': Policy.objects.all()
    }

    return render(request, 'new_policy.html', context)


@login_required(login_url='/accounts/')
def create_a_policy(request):
    organization = request.POST["organization"]
    policy = request.POST["policy"]
    affectedResource = request.POST["affectedResource"]
    metadata = request.POST["metadata"]
    actionItem = request.POST["actionItem"]
    resourceTagToNotify = (request.POST["resourceTagToNotify"]).toLowerCase()
    ActivatedPolicy.objects.create(organization=organization, policy=policy, affectedResource=affectedResource,
                                   metadata=metadata, actionItem=actionItem, resourceTagToNotify=resourceTagToNotify)
    return HttpResponseRedirect(my_policies)


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
