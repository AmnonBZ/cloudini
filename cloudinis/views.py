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