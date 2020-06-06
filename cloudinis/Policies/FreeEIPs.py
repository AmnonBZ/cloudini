from cloudinis.models import *
import boto3

# Currently - only applies to S3

def FreeEIPs(customer, policy):
    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]

    invalid = []

    for region in regionList:

        # try:
        #     activated_policies = ActivatedPolicy.objects.get(customer=customer, policy=policy)
        # except ActivatedPolicy.DoesNotExist:
        #     activated_policies = None

        client = boto3.client('ec2', region_name=region)
        response = client.describe_addresses()
        for address in response["Addresses"]:
            try:
                address["InstanceId"]
            except KeyError:
                invalid.append(address["AllocationId"])

    return invalid
