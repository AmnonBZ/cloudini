from django.shortcuts import render
from . import tempData
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from cloudinis.policies.scan import *


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
def policies(request):
    try:
        policiesList = ActivatedPolicy.objects.all().filter(organization=request.user.id)
    except ValueError:
        policiesList = []

    return render(request, 'policies.html', {
        "policiesList": policiesList
    })
0

@login_required(login_url='/accounts/')
def violations(request):
    violationsList = Violation.objects.all().filter(connectedPolicy__organization=request.user.id, isFixed=False).order_by("date")
    return render(request, 'violations.html', {
        "violationsList": violationsList
    })


@login_required(login_url='/accounts/')
def scan(request):
    x = scan_for_violations(request.user.id)

    return render(request, 'scan.html', {
        "x": x
    })

@login_required(login_url='/accounts/')
def view_policies(request):
    context = {
        'all_policies': tempData.all_policies,
        'types': tempData.policyType,
        'a': [tempData.EC2_policies, tempData.S3_policies],
        'range' : range(10)
    }
    return render(request, 'view_policies.html', context)

@login_required(login_url='/accounts/')
def new_policy(request):
    context = {
        'all_policies': tempData.all_policies,
    }
    return render(request, 'new_policy.html', context)