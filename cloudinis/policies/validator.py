import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys

def calculate(resource_id, activatedPolicy, user, region):
    validator = Violation.objects.get(connectedPolicy=activatedPolicy, resource_id=resource_id)

    if validator:
        validator.isChecked = True
        validator.isFixed = False
        for action_item in activatedPolicy.actionItem:
            if action_item == "notify":
                validator.notify(user.email)
            if action_item == "delete":
                validator.delete_me(user, region)

        validator.save()
    else:
        create_violation(resource_id, activatedPolicy, user, region)


def create_violation(resource_id, activatedPolicy, user, region):
    new_violation = Violation.objects.create(connectedPolicy=activatedPolicy, resource_id=resource_id,
                             date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True, isFixed=False)

    for action_item in activatedPolicy.actionItem:
        if action_item == "notify":
            new_violation.notify("amnon.bn1992@gmail.com")
        if action_item == "delete":
            new_violation.delete_me(user, region)


def validator(resource_id, activatedPolicy, user, region):
    try:
        try:
            try:
                calculate(resource_id, activatedPolicy, user, region)
            except ObjectDoesNotExist:
                create_violation(resource_id, activatedPolicy, user, region)

        except KeyError:
            try:
                calculate(resource_id, activatedPolicy, user, region)
            except ObjectDoesNotExist:
                create_violation(resource_id, activatedPolicy, user, region)
    except:
        return sys.exc_info()
