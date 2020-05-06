import boto3
from cloudinis.models import *

def Naming(customer, policy):
    region = 'us-east-1'
    invalid = []

    client = boto3.client('ec2', region_name=region)

    # response = client.describe_instances(Filters=[{'Name': 'tag: Name', 'Values': ['']}])
    # invalid.append(response)

    # for instance in response:
    #     if not instance[0]['Reservations'][0]['Instances']['State']['Name'] == 'terminated':
    #invalid.append(response['ResponseMetadata']['HTTPHeaders']['server'])



    return invalid
