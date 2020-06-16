import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

aws_access_key_id='ASIARZNQPU7KZ37ZVMFP'
aws_secret_access_key='JbIKdz3xpnszYOkcLfQnenr8DBF6OcSKB5U59U44'
aws_session_token='FwoGZXIvYXdzEFcaDKlSAzgZqx0HhvIBfCLDAZ29422Gegdir/VnBqdT9qjEL0ChYgBSLgewCek1NHaJjNMLpmGiB5a7yisH3IABgaQ6Z2yP2V22P1Vh0Uegkb7P11tEny2OvGUeEq3jKRZQwSTUqT5XfpqyqnLAC+o0Aibb2XtFAdckkpVqM4Q3pM5LQio6la/vo1mu5EG3Rq/aEfD4Ka01OCTVrOt5T9tPI7f1Zx0WBfEe4LnYVm/n5311urhFAr/d0hPTTDfaAV78TvQtzOiKkpYzRfrtJ/exSHmi9Si4l6P3BTIt0MZHFCCo6XTCAw82bOtAsGTHTBLOFAuEh6QYr+voo1zAfo6seiZPi3a1Go5x'

def resourceHandler(resource, region):
    return boto3.resource(resource, region_name=region,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,aws_session_token=aws_session_token)

def clientHandler(resource, region):
    return boto3.client(resource, region_name=region,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,aws_session_token=aws_session_token)

def clientApply(resource, wheretorun):
    regionList = ["us-east-1"]
    for region in regionList:
        client = clientHandler(resource, region)

        if wheretorun == "list_buckets":
            response = client.list_buckets()
        if wheretorun == "describe_instances":
            response = client.describe_instances()
        if wheretorun == "describe_volumes":
            response = client.describe_volumes()
        if wheretorun == "describe_addresses":
            response = client.describe_addresses()

        return response


