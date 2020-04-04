from django.shortcuts import render
from django.utils import timezone
from cloudinis.Policies.TagEnforcement import TagEnforecement


# Create your views here.
def index(request):
    invalid = TagEnforecement(1, 1)
    return render(request, 'main/index.html', {
        "invalid": invalid
    })
