from cloudinis.Policies.clientApply import *
from cloudinis.Policies.validator import *
import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

####ammnon created it, need to be tested - TODO

def FreeEIPs(activatedPolicy):
    response = clientApply("ec2", "describe_addresses")
#--------------------------------------------------------------------------------------------
    for address in response["Addresses"]:
        try:
            address["InstanceId"]
        except KeyError:
#--------------------------------------------------------------------------------------
            validator("AllocationId", address, activatedPolicy)
    return "Finished succesfully"