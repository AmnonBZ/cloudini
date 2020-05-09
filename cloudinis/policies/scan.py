from datetime import datetime

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



def scan_for_violations(organization):

# Before operations
    allViolations = Violation.objects.all()
    for violation in allViolations:
        violation.isChecked = False
        violation.save()

    customerActivatedPolicy = ActivatedPolicy.objects.filter(organization=organization)

    if customerActivatedPolicy:
        for activatedPolicy in customerActivatedPolicy:
            if "AttachedVolumes" in activatedPolicy.policy.name:
                output = AttachedVolumes(activatedPolicy)
            if "ResourceLocationEC2" in activatedPolicy.policy.name:
                output = ResourceLocationEC2(activatedPolicy)
            if "VolumeEncryptionEC2" in activatedPolicy.policy.name:
                output = VolumeEncryptionEC2(activatedPolicy)
            if "ResourceType" in activatedPolicy.policy.name:
                output = ResourceType(activatedPolicy)
            if "TagEnforcementS3" in activatedPolicy.policy.name:
                output = TagEnforcementS3(activatedPolicy)
            if "TagEnforcementEC2" in activatedPolicy.policy.name:
                output = TagEnforcementEC2(activatedPolicy)
            if "NamingPolicy" in activatedPolicy.policy.name:
                output = NamingPolicy(activatedPolicy)
            if "ResourceLocationS3" in activatedPolicy.policy.name:
                output = ResourceLocationS3(activatedPolicy)
            if "FreeEIPs" in activatedPolicy.policy.name:
                output = FreeEIPs(activatedPolicy)
            if "VolumeEncryptionS3" in activatedPolicy.policy.name:
                output = VolumeEncryptionS3(activatedPolicy)


# After operations
    allViolations = Violation.objects.all()
    for violation in allViolations:
        if (violation.isChecked is False) and (violation.isFixed is False):
            violation.isFixed = True
            violation.isChecked = True
            violation.fixedDate = datetime.now().strftime("%F %H:%M:%S")
            violation.save()

        deleteme(violation.resourceName, 'instance')

    return output