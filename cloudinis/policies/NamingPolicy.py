from cloudinis.Policies.validator import *
import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys
import re

# TODO - test it

def NamingPolicy(activatedPolicy):
    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]

    for region in regionList:
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        response = client.describe_volumes()

        if not response == []:
            for reservations in response["Reservations"]:
                for instance in reservations["Instances"]:
                    if not instance['State']['Name'] == 'terminated':
                        if re.search(str(activatedPolicy.metadata), instance["Tags"]["Name"]):
                            validator("InstanceId", instance, activatedPolicy)
    return True