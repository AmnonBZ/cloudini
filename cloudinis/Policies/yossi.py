# from cloudinis.models import *
# import boto3
# # if not response2['InstanceStatuses']['InstanceState']['Code'] == '48':
# #response2 = client.describe_instance_status()
#
# def yossi(customer, policy):
#     # regionList = ["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ap-east-1", "ap-south-1", "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "me-south-1", "sa-east-1"]
#     regionList = ["us-east-1"]
#     invalid = []
#     each_ID=[]
#     for region in regionList:
#         try:
#             activated_policies = ActivatedPolicy.objects.get(customer=customer, policy=policy)
#         except ActivatedPolicy.DoesNotExist:
#             activated_policies = None
#
#         client = boto3.client('ec2', region_name=region)
#         resource = boto3.resource('ec2', region_name=region)
#         response = client.describe_instances()
#
# ###checking if there are any instances on the specific region (which arn't allowed to exist)
#         if not response["Reservations"][0]["Instances"] == []:
#             for instance in response["Reservations"]:
#                 each_ID.append(instance["Instances"][0]["InstanceId"])
#                 #each instance that isnt supposed to be here will be marked using "each_ID" array
# ###checking if the instance is "terrminated":
#                 #only if it's not "Terrminated" it will be sent to the "invalid" array
#             for status in resource.meta.client.describe_instance_status()['InstanceStatuses']:
#                 if status['InstanceState']['Code'] == '48':
#                     invalid.append(status['InstanceId'])
#                 else:
#                     return "all good"
#
#
#     return invalid

                #if not client.describe_instance_status(InstanceIds=ids)['InstanceStatuses']['InstanceState']['Code'] == '48':
                #     invalid.append(instance['InstanceId'])
                # else:
                #     return "all good"
                # for instance in response["Reservations"][0]["Instances"]:
                #     r = client.describe_instance_status(InstanceIds=instance)
                #     if r['InstanceStatuses']['InstanceState']['Code'] == '48':
                #         invalid.append(instance)
#------------------------------------------------------------------------------
        #ec2 = boto3.resource('ec2', region_name=region)
        #for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
        #    if status['InstanceState']['Code'] == 16:
        #        invalid.append(status['InstanceId'])
#------------------------------------------------------------------------------

