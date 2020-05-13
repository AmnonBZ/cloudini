from cloudinis.Policies.clientApply import *
from cloudinis.Policies.validator import *
import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

def VolumeEncryptionEC2(activatedPolicy):
    response = clientApply("ec2", "describe_volumes")
    # --------------------------------------------------------------------------------------------
    for volume in response["Volumes"]:
        if not volume["Encrypted"]:
    # --------------------------------------------------------------------------------------
            validator("VolumeId", volume, activatedPolicy)


    return "Finished succesfully"




    # regionList = ["us-east-1"]
    # try:
    #     for region in regionList:
    #         client = boto3.client('ec2', region_name="us-east-1", aws_access_key_id="ASIARZNQPU7KUL3QKR4O",
    #                               aws_secret_access_key="lmEAu76UwkbkPrZ+dfjV6buxuUsqd2/U3/8OCiLP",
    #                               aws_session_token="FwoGZXIvYXdzEA0aDKXGWuYpBgO/tgr32iLDAaNGMA4Sh62RdWI4ufO/1ohRvdsIPDF5H5jaJOzpE/AotX1hH7dK6hRN5xvpABDp+S0g3zRlgHqEfuseCtgUZRMgsd+xGt2YPL+ssVOL10nz7djFJBYhZCU37iLQqSl6OCWzP/fySdCJPhJYz+F7+k01rJxXVyrcm1D5Zgdm92WkK8ERm0f//6eymjv2m1q711aYcAkirloarlZzmKDDM3VjeIsaldAn3DXLkmuXd46iuGNqtNNYVdnVjyEWq9NoEU4e0Sjih+r1BTIt+8hu5M1vKHILbw/OW1aaSPInR/WcNiEPIFmPdj8r9XRq4Gjbu97K5S+E3jZn")
    #         response = client.describe_volumes()
    #         for instance in response["Volumes"]:
    #             if not instance["Encrypted"]:
    #                 try:
    #                     try:
    #                         validator = Violation.objects.get(connectedPolicy=activatedPolicy,
    #                                                           resourceName=instance["VolumeId"])
    #                         if validator:
    #                             validator.isChecked = True
    #                             validator.isFixed = False
    #                             validator.save()
    #                         else:
    #                             Violation.objects.create(connectedPolicy=activatedPolicy,
    #                                                      resourceName=instance["VolumeId"],
    #                                                      date=datetime.now().strftime("%F %H:%M:%S"),
    #                                                      isChecked=True,
    #                                                      isFixed=False)
    #
    #                     except ObjectDoesNotExist:
    #                         Violation.objects.create(connectedPolicy=activatedPolicy,
    #                                                  resourceName=instance["VolumeId"],
    #                                                  date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
    #                                                  isFixed=False)
    #
    #                 except KeyError:
    #                     try:
    #                         validator = Violation.objects.get(connectedPolicy=activatedPolicy, resourceName=instance["VolumeId"])
    #                         if validator:
    #                             validator.isChecked = True
    #                             validator.isFixed = False
    #                             validator.save()
    #                         else:
    #                             Violation.objects.create(connectedPolicy=activatedPolicy,resourceName=instance["VolumeId"],date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,isFixed=False)
    #                     except ObjectDoesNotExist:
    #                             Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=instance["VolumeId"],date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,isFixed=False)
    # except:
    #     return sys.exc_info()
    #
    # return "Finished succesfully"