import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

# Currently - only applies to EC2

def TagEnforcement(activatedPolicy):

    # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
    regionList = ["us-east-1"]
    try:
        for region in regionList:

            client = boto3.client('ec2', region_name="us-east-1", aws_access_key_id="",
                                  aws_secret_access_key="",
                                  aws_session_token="")
            response = client.describe_instances()
            for instance in response["Reservations"][0]["Instances"]:
                instanceKeys = []
                try:
                    for tag in instance["Tags"]:
                        instanceKeys.append(tag["Key"])

                    if not set(activatedPolicy.metadata).issubset(set(instanceKeys)):
                        try:
                            validator = Violation.objects.get(connectedPolicy=activatedPolicy,
                                                              resourceName=instance["InstanceId"])
                            if validator:
                                validator.isChecked = True
                                validator.isFixed = False
                                validator.save()
                            else:
                                Violation.objects.create(connectedPolicy=activatedPolicy,
                                                         resourceName=instance["InstanceId"],
                                                         date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
                                                         isFixed = False)

                        except ObjectDoesNotExist:
                            Violation.objects.create(connectedPolicy=activatedPolicy,
                                                     resourceName=instance["InstanceId"],
                                                     date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
                                                     isFixed = False)


                except KeyError:
                    try:
                        validator = Violation.objects.get(connectedPolicy=activatedPolicy,
                                                          resourceName=instance["InstanceId"])
                        if validator:
                            validator.isChecked = True
                            validator.isFixed = False
                            validator.save()
                        else:
                            Violation.objects.create(connectedPolicy=activatedPolicy,
                                                     resourceName=instance["InstanceId"],
                                                     date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
                                                     isFixed = False)

                    except ObjectDoesNotExist:
                        Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=instance["InstanceId"],
                                                 date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
                                                 isFixed = False)
    except:
        return sys.exc_info()

    return "Finished succesfully"