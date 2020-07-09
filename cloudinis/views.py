from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import *
from .models import *
from .decorators import org_admin_only, unauthenticated_user
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from cloudinis.Policies.scan import *
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django import forms
from django.db import models
import datetime

from django.contrib.auth.models import User, Group, Permission


@login_required(login_url='/login/')
def home(request):
    print(datetime.datetime.now() - datetime.timedelta(days=1))
    policies = Policy.objects.all()
    activatedPolicies = ActivatedPolicy.objects.all().filter(organization_id=request.user.organization_id)
    violations = Violation.objects.all().filter(connectedPolicy__in=activatedPolicies)

    # data1
    fixed = violations.filter(isFixed=True).count()
    notFixed = violations.filter(isFixed=False).count()

    #data2
    v_ap = []
    policies_names = []
    for ap in activatedPolicies:

        v_ap.append(violations.filter(connectedPolicy=ap).count())
        policies_names.append(ap.policy.name +"-"+ap.affectedResource)

    # data3
    d3=[]
    months= [ "August", "September","October","November","December","January", "February", "March", "April","May","June","July"]

    # for i in 12:
    #     for v in violations:
    #         if v.date

    # data4

    context = {
        'policies': policies,
        'data1': [fixed, notFixed],
        'data2': v_ap,
        'labels2': policies_names,
        # 'data3':,
    }

    next_url = request.GET.get('next')
    if next_url=="/profile/":
        return profile(request)


    return render(request, 'home.html', context)

def view_policies(request):
    policies = Policy.objects.all()

    context = {
        'policies': policies,
    }

    return render(request, 'view_policies.html', context)


def about(request):
    return render(request, 'about.html')


# @login_required(login_url='/login/')
# def policies(request):
#     try:
#         policiesList = ActivatedPolicy.objects.all().filter(organization=request.user.organization_id)
#     except ValueError:
#         policiesList = []
#
#     return render(request, 'policies.html', {
#         "policiesList": policiesList
#     })


@login_required
def violations(request):
    violationsList = Violation.objects.all().filter(connectedPolicy__organization=request.user.organization_id,
                                                    isFixed=False).order_by("date")
    scan_status = request.user.organization.scan_status
    last_scan_time = request.user.organization.last_scan_time

    if scan_status == "Finished successfully":
        messages.success(request, scan_status)
    else:
        messages.warning(request, scan_status)

    return render(request, 'violations.html', {
        "violationsList": violationsList,
        "last_scan_time": last_scan_time
    })


@login_required
def scan(request):
    scan_result = scan_for_violations(request.user)
    org = Organization.objects.get(name=request.user.organization)
    org.scan_status = scan_result[0:499]
    org.last_scan_time = datetime.datetime.now().strftime("%F %H:%M:%S")
    org.save(update_fields=['scan_status', 'last_scan_time'])
    return redirect('violations')


class PolicyListView(ListView):
    model =  ActivatedPolicy
    template_name = 'cloudinis/policies.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'policies'
    ordering = ['-policy']


class PolicyCreateView(LoginRequiredMixin, CreateView):
    model = ActivatedPolicy
    fields = ['policy','affectedResource', 'metadata', 'actionItem', 'resourceTagToNotify']

    def form_valid(self,form):
        form.instance.organization_id = self.request.user.organization_id
        return super().form_valid(form)

class PolicyUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = ActivatedPolicy
    fields = ['policy', 'affectedResource', 'metadata', 'actionItem', 'resourceTagToNotify']

    def form_valid(self, form):
        form.instance.organization_id = self.request.user.organization_id
        return super().form_valid(form)

    def test_func(self):
        policy = self.get_object()
        if self.request.user.organization_id == policy.organization_id:
            return True
        return False


class PolicyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ActivatedPolicy
    success_url = '/policies'

    def form_valid(self, form):
        form.instance.organization_id = self.request.user.organization_id
        return super().form_valid(form)

    def test_func(self):
        policy = self.get_object()
        if self.request.user.organization_id == policy.organization_id:
            return True
        return False


class OrganizationCreateView(SuccessMessageMixin,CreateView):
    model = Organization
    fields = ['name']

    success_message = "Please login for the first time with username: admin_%(name)s and password: changeme"
    def get_success_url(self):
        return reverse('profile')

@org_admin_only
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.organization_id = request.user.organization_id
            new_user.is_active = True
            new_user.access_key = request.user.access_key
            new_user.secret_key = request.user.secret_key
            new_user.session_token = request.user.session_token
            new_user.save()
            messages.success(request, f'The user has been added successfully !')
            # return HttpResponse("<h1>Thanks for registering, Cloudinis's team will contact you soon</h1>")
            return render(request, 'registration/register.html', {'form': form})
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


@login_required
def change_password(request):
     if request.method == 'POST':
         form = PasswordChangeForm(data=request.POST, user=request.user)

         if form.is_valid():
             form.save()
             update_session_auth_hash(request, form.user)
             messages.success(request, f'Your password has been updated successfully !')
             return redirect('profile')
     else:
         form = PasswordChangeForm(user=request.user)
     context = {
         'form': form,
     }
     return render(request, 'registration/change_password.html', context)


