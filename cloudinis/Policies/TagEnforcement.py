from cloudinis.models import *
import boto3

def TagEnforecement(customer, policy):
    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]

    invalid = []

    for region in regionList:

        activated_policies = ActivatedPolicy.objects.get(customer=customer, policy=policy)

        client = boto3.client('ec2', region_name=region)
        response = client.describe_instances()
        for instance in response["Reservations"][0]["Instances"]:
            instanceKeys = []
            try:
                for tag in instance["Tags"]:
                    instanceKeys.append(tag["Key"])

                if not set(activated_policies.metadata).issubset(set(instanceKeys)):
                    invalid.append(instance["PublicDnsName"])
            except KeyError:
                invalid.append(instance["PublicDnsName"])

    return invalid
