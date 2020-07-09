import boto3
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from cloudinis.models import *
import sys


def validator(whatkindof, index, activatedPolicy):
    try:
        try:
            try:
                validator = Violation.objects.get(connectedPolicy=activatedPolicy, resourceName=index[whatkindof])

                if validator:
                    validator.isChecked = True
                    validator.isFixed = False
                    validator.save()
                else:
                    Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=index[whatkindof], date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True, isFixed=False)

            except ObjectDoesNotExist:
                    Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=index[whatkindof], date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True, isFixed=False)

        except KeyError:
            try:
                validator = Violation.objects.get(connectedPolicy=activatedPolicy, resourceName=index[whatkindof])

                if validator:
                    validator.isChecked = True
                    validator.isFixed = False
                    validator.save()
                else:
                    Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=index[whatkindof], date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True, isFixed=False)

            except ObjectDoesNotExist:
                Violation.objects.create(connectedPolicy=activatedPolicy, resourceName=index[whatkindof], date=datetime.now().strftime("%F %H:%M:%S"), isChecked=True, isFixed=False)
    except:
        return sys.exc_info()
