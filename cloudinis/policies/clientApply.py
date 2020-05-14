import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

aws_access_key_id="ASIARZNQPU7KW6WFIOE3"
aws_secret_access_key="YBaxNzhQR1Gl5ZoOC7CEGRBh/Xho8dp46j54nRT2"
aws_session_token="FwoGZXIvYXdzEDsaDJe6PNwQoQdY0J0LdiLDAb/5dFD0xgYfRv6HeLbE4PZwW5TXwjATfZCxQWqgwFVmYBqKBX1hTcpTqoa5AiiNQFjFWv+JamzO/TCaTI9eT4j22p/aiYz+BI5aN+ByBWt99PB5oWs2oHY07qlU9+h1md6AZGtlSoqYPDDJRg32Ns8iJ+/vUPRFbmNkOlkcuB4HQQs1pJtvpmvOdMPqupzP1WntTvCKWfxZkPqcOy8zO2jsq/ugS8vGk1Iwj6mYNtseTosJhljYQ2YKrs5/dQ2oIw7VZijupfT1BTItW8oJd32hgUkuO9bABRtjp5GXoaRlCMhAZqVqGFbvR0iJWeDlGkQJTyunfonD"

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


