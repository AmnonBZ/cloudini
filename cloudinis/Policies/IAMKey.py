from cloudinis.models import *
import boto3


def IAMKey(customer, policy):
    regionList = ["us-east-1"]
    invalid = []
    for region in regionList:
        try:
            activated_policies = ActivatedPolicy.objects.get(customer=customer, policy=policy)
        except ActivatedPolicy.DoesNotExist:
            activated_policies = None
        client = boto3.client('iam', region_name=region)
        resource = boto3.resource('iam')
        boto3.setup_default_session(profile_name='IAM')
        KEY = 'LastUsedDate'
        for user in resource.users.all():
            Metadata = client.list_access_keys(UserName=user.user_name)
            if Metadata['AccessKeyMetadata']:
                for key in user.access_keys.all():
                    AccessId = key.access_key_id
                    Status = key.status
                    LastUsed = client.get_access_key_last_used(AccessKeyId=AccessId)
                    if (Status == "Active"):
                        if KEY in LastUsed['AccessKeyLastUsed']:
                            print
                            "User: ", user.user_name, "Key: ", AccessId, "AK Last Used: ", \
                            LastUsed['AccessKeyLastUsed'][KEY]
                        else:
                            print
                            "User: ", user.user_name, "Key: ", AccessId, "Key is Active but NEVER USED"
                    else:
                        print
                        "User: ", user.user_name, "Key: ", AccessId, "Keys is InActive"
            else:
                print
                "User: ", user.user_name, "No KEYS for this USER"
    return invalid
