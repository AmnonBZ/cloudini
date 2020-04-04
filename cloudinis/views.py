from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import *
import boto3


# Create your views here.
def index(request):
    invalid = []
    client = boto3.client('ec2', region_name="us-east-1")
    response = client.describe_instances()
    for i in response["Reservations"]:
        try:
            for j in i["Instances"][0]["Tags"]:
                if not j["Key"] == "Owner":
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 1:
                invalid.append(i["Instances"][0]["PublicDnsName"])
        except KeyError:
            invalid.append(i["Instances"][0]["PublicDnsName"])
    # invalid = ["1", "2", "3"]

    return render(request, 'main/index.html', {
        "invalid": invalid
    })
