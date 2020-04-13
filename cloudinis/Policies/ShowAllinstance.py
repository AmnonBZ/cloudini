from cloudinis.models import *
import boto3


def ShowAllinstance(customer, policy):
    regionList = ["us-east-1"]
    for region in regionList:
        client = boto3.client('ec2', region_name=region)
        response = client.describe_instances()
    return response
