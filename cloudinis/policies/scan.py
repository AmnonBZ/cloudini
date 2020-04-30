from datetime import datetime

from cloudinis.models import *
from .TagEnforcement import TagEnforcement

def scan_for_violations(organization):

# Before operations
    allViolations = Violation.objects.all()
    for violation in allViolations:
        violation.isChecked = False
        violation.save()

    customerActivatedPolicy = ActivatedPolicy.objects.filter(organization=organization)

    if customerActivatedPolicy:
        for activatedPolicy in customerActivatedPolicy:
            if "TagEnforcement" in activatedPolicy.policy.name:
                output = TagEnforcement(activatedPolicy)

# After operations
    allViolations = Violation.objects.all()
    for violation in allViolations:
        if (violation.isChecked is False) and (violation.isFixed is False):
            violation.isFixed = True
            violation.isChecked = True
            violation.fixedDate = datetime.now().strftime("%F %H:%M:%S")
            violation.save()

    return output