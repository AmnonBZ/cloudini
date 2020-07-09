import boto3
from cloudinis.policies.validator import *
from botocore.exceptions import *

def ResourceLocationEC2(user, activatedPolicy):
    regionList = activatedPolicy.metadata

    for region in regionList:
        try:
            client = boto3.client('ec2', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                                  aws_session_token=user.session_token, region_name=region)
            response = client.describe_instances()

            if not response == []:
                for reservation in response['Reservations']:
                    for instance in reservation['Instances']:
                        if not instance['State']['Name'] == 'terminated':
                            validator("InstanceId", instance, activatedPolicy)
        except Exception:
            return "{region} is invalid to use by the specified access key".format(region=region)

    return True