from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from accounts.models import CloudiniUser
from django.urls import reverse

class Policy(models.Model):
    name = models.CharField(max_length=200)
    affectedResources = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return self.name


class ActivatedPolicy(models.Model):
    organization = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    affectedResource = models.CharField(max_length=200 ,  verbose_name="Resource")
    metadata = ArrayField(models.CharField(max_length=200,),verbose_name="What to enforce")
    actionItem = ArrayField(models.CharField(max_length=200), verbose_name="Action item")
    resourceTagToNotify = ArrayField(models.CharField(max_length=200), verbose_name="Tag to enforce")

    def __str__(self):
        return "{}-{}-{}".format(self.organization, self.policy, self.affectedResource)

    def get_absolute_url(self):
        return reverse('policies')


class Violation(models.Model):
    connectedPolicy = models.ForeignKey(ActivatedPolicy, on_delete=models.CASCADE)
    resourceName = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) #TODO
    isChecked = models.BooleanField(default=False)
    isFixed = models.BooleanField(default=False)
    fixedDate = models.DateTimeField(default=None, null=True)