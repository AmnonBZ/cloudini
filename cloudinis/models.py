from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CloudiniUser(AbstractUser):
    class Meta:
        unique_together = ('username', 'email')

    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.is_active = False
        super(CloudiniUser, self).save(*args, **kwargs)


    def __str__(self):
        return self.username


class Policy(models.Model):
    name = models.CharField(max_length=200)
    affectedResources = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return self.name


class ActivatedPolicy(models.Model):
    organization = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    affectedResource = models.CharField(max_length=200)
    metadata = ArrayField(models.CharField(max_length=200))
    actionItem = ArrayField(models.CharField(max_length=200))
    resourceTagToNotify = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return "{}-{}-{}".format(self.organization, self.policy, self.affectedResource)


class Violation(models.Model):
    connectedPolicy = models.ForeignKey(ActivatedPolicy, on_delete=models.CASCADE)
    resourceName = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True) #TODO
    isChecked = models.BooleanField(default=False)
    isFixed = models.BooleanField(default=False)
    fixedDate = models.DateTimeField(default=None, null=True)