from cloudinis.models import *
import boto3

def ResourceLocationEC2(customer, policy):
    regionList = ["us-east-1"]
    for region in regionList:
        invalid = []
        # try:
        #     activated_policies = ActivatedPolicy.objects.get(customer=customer, policy=policy)
        # except ActivatedPolicy.DoesNotExist:
        #     activated_policies = None

        client = boto3.client('ec2', region_name=region)
        response = client.describe_instances()

# checking if there are any instances on the specific region (which arn't allowed to exist)
        if not response == []:

            for i in response['Reservations']:
                for j in i['Instances']:
                ###we are checking if there is an living instance (not terminated) in the current region
                ###only if it's not "Terrminated" it will be sent to the "invalid" array
                    if not j['State']['Name'] == 'terminated':
                        invalid.append(j['InstanceId'])


    return invalid

# for instance in response["Reservations"][0]["Instances"]:
#     if not instance['State']['Name'] == 'terminated':
#         invalid.append(instance['InstanceId'])