from cloudinis.models import *
import boto3

# Currently - only applies to EC2

def ResourceType(customer, policy):
    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]
    invalid = []

    for region in regionList:

        client = boto3.client('ec2', region_name=region)
        response = client.describe_instances()

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                invalid.append(instance['InstanceType'])

        return invalid


    #     try:
    #         activated_policies = ActivatedPolicy.objects.get(customer=customer, policy=policy)
    #     except ActivatedPolicy.DoesNotExist:
    #         activated_policies = None
    #     instanceKeys = []
    #     client = boto3.client('ec2', region_name=region)
    #     response = client.describe_instances()
    #
    #     for reservation in response["Reservations"]:
    #         for instance in reservation["Instances"]:
    #             try:
    #                 for type in instance["Tags"]:
    #                     instanceKeys.append(type["Key"])
    #
    #                 if not set(activated_policies.metadata).issubset(set(instanceKeys)):
    #                     invalid.append(instance["InstanceType"])
    #             except KeyError:
    #                 invalid.append(instance["InstanceType"])
    #
    # return invalid
