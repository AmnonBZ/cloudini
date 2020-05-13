from cloudinis.Policies.clientApply import *
from cloudinis.Policies.validator import *
import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys


###### NEEDED TO BE FIXED!!!

def ResourceLocationS3(activatedPolicy):
    response = clientApply("s3", "list_buckets")

    # --------------------------------------------------------------------------------------------
    if not response["Buckets"] == []:
        for bucket in response["Buckets"]:
    # --------------------------------------------------------------------------------------
            validator("Name", bucket, activatedPolicy)


    return "Finished succesfully"






        # regionList = ["us-east-1"]
        # bucketsName = []
        # try:
        #      for region in regionList:
        #          client = boto3.client('s3', region_name="us-east-1", aws_access_key_id="ASIARZNQPU7K2SDULI6R",
        #                       aws_secret_access_key="+6rcbEObSkJ4g+9YoCsVfKA3qazzsl90JSeXEHon",
        #                       aws_session_token="FwoGZXIvYXdzEBAaDP0Ti6qlVf3nnJiSlSLDAawCsjZ7qGlahKmx+eY0xY/Mxk76D+WmrOFT4X9wI0mpWG/sVJN/JbieyIQ12q+eLCUJObrarkrdSk8KeQbGmt6uMV2+sGAZpywRTBXBsi0KDgYNEjRZ+87gDYY9lfi+NLLXNoP+O4rdalbgm84K5CY3EdDrgfoPsLqIWoIu+HnN9L7D85eloknLqcnVi75mJDqMdLP684FiccWuaIzc5tNt/aEFDVXbqtJgV3pLAvLaznP+KovSOAI6HWxD3Lplbl+yWSjf4er1BTIt0LiGk5jIob2gaQlczzRaTG289333EMlFMpGwl02W7Lm8aJWxMLc3xR1ZTfP/")
        #          response = client.list_buckets()
        #          if not response["Buckets"] == []:
        #             for instance in response["Buckets"]:
        #                 bucketsName.append(instance["Name"])
        #                 if not set(activatedPolicy.metadata).issubset(set(bucketsName)):
        #                     try:
        #                         try:
        #                             validator = Violation.objects.get(connectedPolicy=activatedPolicy,
        #                                                             resourceName=instance["Name"])
        #                             if validator:
        #                                  validator.isChecked = True
        #                                  validator.isFixed = False
        #                                  validator.save()
        #                             else:
        #                                  Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=instance["Name"],
        #                                          date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
        #                                          isFixed=False)
        #
        #                         except ObjectDoesNotExist:
        #                                 Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=instance["Name"],
        #                                      date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
        #                                      isFixed=False)
        #
        #                     except KeyError:
        #                         try:
        #                               validator = Violation.objects.get(connectedPolicy=activatedPolicy,
        #                                                       resourceName=instance["Name"])
        #                               if validator:
        #                                  validator.isChecked = True
        #                                  validator.isFixed = False
        #                                  validator.save()
        #                               else:
        #                                      Violation.objects.create(connectedPolicy=activatedPolicy,
        #                                      resourceName=instance["Name"],
        #                                      date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
        #                                     isFixed=False)
        #                         except ObjectDoesNotExist:
        #                                             Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=instance["Name"],
        #                                              date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True,
        #                                              isFixed=False)
        #
        # except:
        #     return sys.exc_info()
        #
        # return "Finished succesfully"
        #
