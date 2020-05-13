import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys


def clientHandler(resource, region):
    return boto3.client(resource, region_name=region,
                        aws_access_key_id="ASIARZNQPU7KVGZWIKMT",
                          aws_secret_access_key="+uSfUWozDVgD+YIZOOFhfcuNqUsXa589UuIcq8bw",
                            aws_session_token="FwoGZXIvYXdzEBUaDL2skVKGQOj4mpvyzCLDAY3HHIdo0JJBB3IGK7wJAGrvjRSpSflWrqawkLs/mSfu70fVXKdv/iuWhTQs/fU8SeoABRZEYkWbLM9v8C3sSnAvssaoAEYniw3ZK/Fyebs9ttlk8ZYMgC0QyiJ1ehs8kZalC+/MoJj30njL1ti+Xv+WxHxWs9c074y33LgonO57oYDqOdkHqjdXc8y2PVXgOY+rWgwM0+Kgt25b5YTshw5VBbri66q4ZXdrw8Q/fQa4x8+Ngv230sUmwV3i66BiXAoEMCjx++v1BTItmpmCILHHvdTeyX/Tvrum1zhRIpmvYVM3UZ5UskH+Qs9fUMCkt4JC4JP0VrOK")


def clientApply(resource, wheretorun):

    regionList = ["us-east-1"]
    for region in regionList:
        client = clientHandler(resource, region)

        if wheretorun == "list_buckets":
            response = client.list_buckets()
        if wheretorun == "describe_instances":
            response = client.describe_instances()
        if wheretorun == "describe_volumes":
            response = client.describe_volumes()
        if wheretorun == "describe_addresses":
            response = client.describe_addresses()


        return response





#---------------------------------BUCKETS-------------------------------------------------------
            # if wheretorun == "list_buckets":
            #     response = client.list_buckets()
                    # for instance in response["Buckets"]:
#                         try:
#                             try:
#                                 validator = Violation.objects.get(connectedPolicy=activatedPolicy,
#                                                                   resourceName=instance["Name"])
#                                 if validator:
#                                     validator.isChecked = True
#                                     validator.isFixed = False
#                                     validator.save()
#                                 else:
#                                     Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=instance["Name"],
#                                                              date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
#                                                              isFixed=False)
#
#                             except ObjectDoesNotExist:
#                                 Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=instance["Name"],
#                                                          date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
#                                                          isFixed=False)
#
#                         except KeyError:
#                             try:
#                                 validator = Violation.objects.get(connectedPolicy=activatedPolicy,
#                                                                   resourceName=instance["Name"])
#                                 if validator:
#                                     validator.isChecked = True
#                                     validator.isFixed = False
#                                     validator.save()
#                                 else:
#                                     Violation.objects.create(connectedPolicy=activatedPolicy,
#                                                              resourceName=instance["Name"],
#                                                              date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
#                                                              isFixed=False)
#                             except ObjectDoesNotExist:
#                                 Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=instance["Name"],
#                                                          date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
#                                                          isFixed=False)
# #-------------------------------INSTANCES-------------------------------------------------------
#             if wheretorun == "describe_instances":
#                 response = client.describe_instances()
#
#
# #----------------------------VOLUMES------------------------------------------------------------
#             if wheretorun == "describe_volumes":
#                 response = client.describe_volumes()





