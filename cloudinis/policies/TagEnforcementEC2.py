from cloudinis.Policies.clientApply import *
from cloudinis.Policies.validator import *
import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

def TagEnforcementEC2(activatedPolicy):
    response = clientApply("ec2", "describe_instances")
#--------------------------------------------------------------------------------------------
    for reservations in response["Reservations"]:
        for instance in reservations["Instances"]:
            instanceKeys = []
            try:
                for tag in instance["Tags"]:
                    instanceKeys.append(tag["Key"])
                    if set(activatedPolicy.metadata).issubset(set(instanceKeys)):
#--------------------------------------------------------------------------------------
                        validator("InstanceId", instance, activatedPolicy)
                        break
            except KeyError:
                None
    return "Finished succesfully"




