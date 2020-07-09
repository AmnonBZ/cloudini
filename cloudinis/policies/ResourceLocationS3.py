import boto3
from cloudinis.policies.validator import *
from botocore.exceptions import *

def ResourceLocationS3(user, activatedPolicy):
    regionList = activatedPolicy.metadata

    for region in regionList:
        try:
            client = boto3.client('s3', aws_access_key_id=user.access_key, aws_secret_access_key=user.secret_key,
                                  aws_session_token=user.session_token, region_name=region)
            response = client.list_buckets()

            if not response["Buckets"] == []:
                for bucket in response["Buckets"]:
                    validator("Name", bucket, activatedPolicy)
        except Exception:
            return "{region} is invalid to use by the specified access key".format(region=region)

        return True