from cloudinis.models import *
import boto3


def ShowAllBuckets(customer, policy):
    regionList = ["us-east-1"]
    for region in regionList:
        client = boto3.client('s3', region_name=region)
        response = client.list_buckets()
    return response
