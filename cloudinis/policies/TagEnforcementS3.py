
# לשאול את אמנון למה צריך את זה: כי גם ככה לכל באקט בהכרח יש גם שם




from cloudinis.models import *
import boto3


# Currently - only applies to EC2


def TagEnforcementS3(customer, policy):
    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]
    invalid = []
    bucketsName = []

    for region in regionList:
        try:
            activated_policies = ActivatedPolicy.objects.get(customer=customer, policy=policy)
        except ActivatedPolicy.DoesNotExist:
            activated_policies = None

        client = boto3.client('s3', region_name=region)
        response = client.list_buckets()
        for i in response["Buckets"]:
            try:
                bucketsName.append(i["Name"])
                if not set(activated_policies.metadata).issubset(set(bucketsName)):
                    invalid.append(i["Name"])

            except KeyError:
                invalid.append(i["Name"])

    return invalid
