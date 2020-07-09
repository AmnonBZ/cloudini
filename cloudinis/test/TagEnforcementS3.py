import boto3
from cloudinis.Policies.validator import *

def TagEnforcementS3(user, activatedPolicy):
    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]
    bucketsName = []

    for region in regionList:
        client = boto3.client('s3', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                              aws_session_token=user.session_token, region_name=region)
        response = client.list_buckets()

        for bucket in response["Buckets"]:
            bucketKeys = []
            try:
                for tag in bucket["Tags"]:
                    bucketKeys.append(tag["Key"])
                if not set(activatedPolicy.metadata).issubset(set(bucketKeys)):
                    validator("Name", bucket, activatedPolicy)

            except KeyError:
                validator("Name", bucket, activatedPolicy)

    return True