from django.shortcuts import render
from . import tempData
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from cloudinis.policies.scan import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django import forms


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


class PolicyListView(ListView):
    model =  ActivatedPolicy
    template_name = 'policies.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'policies'
    #ordering = ['-date_posted']


class PolicyDetailView(DetailView):
    model = ActivatedPolicy

class PolicyCreateView(LoginRequiredMixin, CreateView):
    model = ActivatedPolicy
    fields = ['organization', 'policy','affectedResource', 'metadata', 'actionItem', 'resourceTagToNotify']


class PolicyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ActivatedPolicy
    success_url = '/policies'


    # def test_func(self):
        # activatedpolicy = self.get_object()
        # if activatedpolicy.organization == self.request.CloudiniUser.id:
        #     return True
        # return False


    def test_func(self):
        return True


