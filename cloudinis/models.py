from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        CloudiniUser.models.objects.create(username="admin", password="changeme", organization=self.id,
                                    email="admin@{organization}.com".format(organization=self.name), isAdmin=True,
                                    access_key="changeme", secret_key="changeme", session_token="changeme")
        super().save(*args, **kwargs)


class CloudiniUser(AbstractUser, models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None, null=True)
    isAdmin = models.BooleanField(default=False)
    access_key = models.CharField(max_length=20)
    secret_key = models.CharField(max_length=50)
    session_token = models.CharField(max_length=400)

    class Meta:
        unique_together = ('username', 'email')

    def __str__(self):
        return self.username

class Policy(models.Model):
    name = models.CharField(max_length=40)
    affectedResources = ArrayField(models.CharField(max_length=200))
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ActivatedPolicy(models.Model):
    organization = models.ForeignKey(CloudiniUser, on_delete=models.CASCADE)
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