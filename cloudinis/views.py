from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
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
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms


@login_required(login_url='/login/')
def home(request):
    policies = Policy.objects.all()
    context = {
        'policies': policies
    }
    return render(request, 'home.html', context)

def view_policies(request):
    policies = Policy.objects.all()
    resources = ['EC2','S3','CloudWatch']


    context = {
        'all_policies': policies,
        'resources' : resources,
    }

    return render(request, 'view_policies.html', context)



def about(request):
    return render(request, 'about.html')


# @login_required(login_url='/login/')
# def policies(request):
#     try:
#         policiesList = ActivatedPolicy.objects.all().filter(organization=request.user.id)
#     except ValueError:
#         policiesList = []
#
#     return render(request, 'policies.html', {
#         "policiesList": policiesList
#     })


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


# class AllPolicyListView(ListView):
#     model =  Policy
#     template_name = 'cloudinis/view_policies.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'policies'
#     ordering = ['-name']

class PolicyListView(ListView):
    model =  ActivatedPolicy
    template_name = 'cloudinis/policies.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'policies'
    ordering = ['-policy']


class PolicyCreateView(LoginRequiredMixin, CreateView):
    model = ActivatedPolicy
    fields = ['policy','affectedResource', 'metadata', 'actionItem', 'resourceTagToNotify']

    def form_valid(self,form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

class PolicyUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = ActivatedPolicy
    fields = ['policy', 'affectedResource', 'metadata', 'actionItem', 'resourceTagToNotify']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        policy = self.get_object()
        if self.request.user == policy.organization:
            return True
        return False


class PolicyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ActivatedPolicy
    success_url = '/policies'

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        policy = self.get_object()
        if self.request.user == policy.organization:
            return True
        return False


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
