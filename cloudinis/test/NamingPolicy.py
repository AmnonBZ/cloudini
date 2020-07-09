from cloudinis.Policies.validator import *
import boto3
import re

def NamingPolicy(user, activatedPolicy):
    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]

    if len(activatedPolicy.metadata) > 1 or (' ' in activatedPolicy.metadata[0]):
        return "An error occurred for the given Regex pattern"

    for region in regionList:
        client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        response = client.describe_instances()
        if not response == []:
            for reservation in response["Reservations"]:
                for instance in reservation["Instances"]:
                    if not instance['State']['Name'] == 'terminated':
                        tags = {}
                        try:
                            for tag in instance['Tags']:
                                tags[tag['Key']] = tag['Value']
                        except KeyError:
                            return "Name tag does not exist on {instance}".format(instance=instance["InstanceId"])

                        if not 'Name' in tags:
                            return "Name tag does not exist on {instance}".format(instance=instance["InstanceId"])
                        else:
                            if not re.search(activatedPolicy.metadata[0], tags['Name']):
                                validator("InstanceId", instance, activatedPolicy)
    return True