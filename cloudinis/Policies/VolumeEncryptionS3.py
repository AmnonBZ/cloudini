from cloudinis.models import *
import boto3
from botocore.exceptions import ClientError


def VolumeEncryptionS3(customer, policy):
    regionList = ["us-east-1"]
    for region in regionList:
        try:
            activated_policies = ActivatedPolicy.objects.get(customer=customer, policy=policy)
        except ActivatedPolicy.DoesNotExist:
            activated_policies = None
            client = boto3.client('s3', region_name=region)
            response = client.list_buckets()
    for bucket in response['Buckets']:
        try:
            enc = client.get_bucket_encryption(Bucket=bucket['Name'])
            rules = enc['ServerSideEncryptionConfiguration']['Rules']
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                print('Bucket: %s, no server-side encryption' % (bucket['Name']))
            else:
                print("Bucket: %s, unexpected error: %s" % (bucket['Name'], e))

