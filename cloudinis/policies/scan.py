from datetime import datetime
# import schedule
# import time
# from celery.schedules import crontab
# from celery.task import periodic_task
# from datetime import timedelta
from cloudinis.models import *
from .ResourceLocationEC2 import ResourceLocationEC2
from .VolumeEncryptionEC2 import VolumeEncryptionEC2
from .TagEnforcementS3 import TagEnforcementS3
from .ResourceType import ResourceType
from .AttachedVolumes import AttachedVolumes
from .remediator import deleteme
from .NamingPolicy import NamingPolicy
from .TagEnforcementEC2 import TagEnforcementEC2
from .ResourceLocationS3 import ResourceLocationS3
from .FreeEIPs import FreeEIPs
from .demo_query import demo_query


def scan_for_violations(user):
# Before operations
    allViolations = Violation.objects.all().filter(connectedPolicy__organization=user.organization_id)
    for violation in allViolations:
        violation.isChecked = False
        violation.save()

    customerActivatedPolicy = ActivatedPolicy.objects.filter(organization=user.organization_id)

    run = demo_query(user)
    if run is not True:
        return run

    if customerActivatedPolicy:
        for activatedPolicy in customerActivatedPolicy:
            if "AttachedVolumes" in activatedPolicy.policy.name:
                run = AttachedVolumes(user, activatedPolicy)
                if run is not True:
                    return run

            if "ResourceLocationEC2" in activatedPolicy.policy.name:
                run = ResourceLocationEC2(user, activatedPolicy)
                if run is not True:
                    return run

            if "VolumeEncryptionEC2" in activatedPolicy.policy.name:
                run = VolumeEncryptionEC2(user, activatedPolicy)
                if run is not True:
                    return run

            if "ResourceType" in activatedPolicy.policy.name:
                run = ResourceType(user, activatedPolicy)
                if run is not True:
                    return run

            if "TagEnforcementS3" in activatedPolicy.policy.name:
                run = TagEnforcementS3(user, activatedPolicy)
                if run is not True:
                    return run

            if "TagEnforcementEC2" in activatedPolicy.policy.name:
                run = TagEnforcementEC2(user, activatedPolicy)
                if run is not True:
                    return run

            if "NamingPolicy" in activatedPolicy.policy.name:
                run = NamingPolicy(user, activatedPolicy)
                if run is not True:
                    return run

            if "ResourceLocationS3" in activatedPolicy.policy.name:
                run = ResourceLocationS3(user, activatedPolicy)
                if run is not True:
                    return run

            if "FreeEIPs" in activatedPolicy.policy.name:
                run = FreeEIPs(user, activatedPolicy)
                if run is not True:
                    return run
    else:
        return "No policies applied"

# After operations
    allViolations = Violation.objects.all().filter(connectedPolicy__organization=user.organization_id)
    for violation in allViolations:
        if (violation.isChecked is False) and (violation.isFixed is False):
            violation.isFixed = True
            violation.isChecked = True
            violation.fixedDate = datetime.now().strftime("%F %H:%M:%S")
            violation.save()

#         if activatedPolicy.actionItem == "deleteme":
#             deleteme(violation.resourceName, "instance")
#         if activatedPolicy.actionItem == "notify":
#             print("skipping")
#     #notify()
#         else:
#             None
#             #todo Couldnt fix by myself :: if activatedPolicy.actionItem == "deleteme"
#             #the problem :: .actionItem is not recognized by the system

    return "Finished successfully"

# organizations = Organization.objects.all()
# for organization in organizations:
#     admin_user = CloudiniUser.objects.get(username="admin_"+organization.name)
#     schedule.every(1).minutes.do(scan_for_violations, user=admin_user)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#
# @periodic_task(run_every=timedelta(seconds=30))
# def scan_every_minute():
#     organizations = Organization.objects.all()
#     for organization in organizations:
#         admin_user = CloudiniUser.objects.get(username="admin_" + organization.name)
#         scan_for_violations(admin_user)