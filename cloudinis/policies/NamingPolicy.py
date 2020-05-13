from cloudinis.Policies.clientApply import *
from cloudinis.Policies.validator import *
import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

######NEEDED TO BE FIXED!!!!

def NamingPolicy(activatedPolicy):
    response = clientApply("ec2", "describe_instances")
#--------------------------------------------------------------------------------------------
    if not response == []:
        for reservations in response["Reservations"]:
            for instance in reservations["Instances"]:
                    if not instance['State']['Name'] == 'terminated':
#--------------------------------------------------------------------------------------
                        validator("InstanceId", instance, activatedPolicy)
    return "Finished succesfully"