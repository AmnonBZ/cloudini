import boto3
from .clientApply import *

def deleteme(resource_id, resource_type):
    if resource_type == "instance":
        client = resourceHandler("ec2", "us-east-1")
        client.instances.filter(InstanceIds=[resource_id]).terminate()

    if resource_type == "volume":
        client = resourceHandler("ec2", "us-east-1")
        client.delete_volume(VolumeId=resource_id)

def notify(resource_id, resource_type):
    if resource_type == "instance":
        print("sending_email")

    if resource_type == "volume":
        print("sending_email")

