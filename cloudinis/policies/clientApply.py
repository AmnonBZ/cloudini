import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

aws_access_key_id='ASIARZNQPU7KTZUMYWNG'
aws_secret_access_key='K3MSf7IPm8AEsNQ4Rjuepltia+evCHIHNXU42YzT'
aws_session_token='FwoGZXIvYXdzEC4aDGoUAinEueRocTrqlCLDATpJWGEleMmByzxXfgVuybXgG8d7ckfPrpmwZfrd1sF8eko21sOcnniPYvQcpvwlbidSTR9kP3dmoCjU0r9QTQ5rtdAmApErXHysQdE5HgDjfvLmHnqF0cV36BKtDzTfpC7HyFEnPbzIRqrNtHLRxJ2HI3PGI5MZbaX1x1E5DOZNZoIFlFHtmMEpA4rqI6XUPPLUrhsxzWuE/FVBm6BiGuZl0FLkbUJ3YZaxRSIMNTOG9vlgqpX8ogjcqDfs83q/TCRQECik4Kn2BTItFNQ7PbjBTvwSr0st5rAX6khsXgKsO7PU1Hf/q+IVYaDyP1uPP0byAiSMuhjg'

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


