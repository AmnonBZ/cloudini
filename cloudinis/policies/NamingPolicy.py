from cloudinis.Policies.clientApply import *
from cloudinis.Policies.validator import *
import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys
import re

# TODO - should support every resource

def NamingPolicy(activatedPolicy):
    response = clientApply("ec2", "describe_instances")
#--------------------------------------------------------------------------------------------
    if not response == []:
        for reservations in response["Reservations"]:
            for instance in reservations["Instances"]:
                if not instance['State']['Name'] == 'terminated':
                    for tag in instance["Tags"]:
                        if re.search(str(activatedPolicy.metadata), tag["Key"]):
#--------------------------------------------------------------------------------------
                            validator("InstanceId", instance, activatedPolicy)
    return "Finished succesfully"