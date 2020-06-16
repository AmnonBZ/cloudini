import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

aws_access_key_id='ASIARZNQPU7K6K7SGDAD'
aws_secret_access_key='35YjrZagskfik2THsEAUNZaYO2+1ARVWvAWnvuHe'
aws_session_token='FwoGZXIvYXdzEFoaDBBDxVUEj/uF92zqvCLDAWQlS7Wm4p4UySh6rGQ9BDH0123W/KQXGF+gRevZG0zeP5B7zlRT0spIDWF3IXZ9sXMP+SdvbzzfyR2XQdzWNacwObGWL0sFB2TqEo/jl2KZKVnTjCrg90R0P8A6AcHr2W4TH2dKujfRTG8P3IIHooiDooR85MQMbOoHobXxUkbEGbxQapfr2Grk9L43N6/LUEfJisfMyhPNbrPZJdbMm/70WwB3CiKLtk0oZk7E8NFYAxuG8M415wUROe6wBkn9mR96FCiA7aP3BTItJcQgV2NaoGs5hjl80eYRT5o+TD5K7Gbq24N6zO0nTNcjHDjBql8i4k8TSDp3'

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


