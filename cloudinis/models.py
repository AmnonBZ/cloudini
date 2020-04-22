from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    main_user_password = models.CharField(max_length=32)

    class Meta:
        unique_together = ('name', 'email')

    def save(self, *args, **kwargs):
        super(Organization, self).save(*args, **kwargs)
        applied_user_model = get_user_model()
        applied_user_model.objects.create(username=self.name, email=self.email, is_active=False,
                                    password=self.main_user_password,
                                    organization=Organization.objects.get(name=self.name))

    def __str__(self):
        return self.name


class CloudiniUser(AbstractUser):
    email = models.EmailField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)


class Policy(models.Model):
    name = models.CharField(max_length=200)
    affectedResources = ArrayField(models.CharField(max_length=200))

    def __str__(self):
        return self.name


class ActivatedPolicy(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    metadata = ArrayField(models.CharField(max_length=200))
    actionItem = models.CharField(max_length=200)


class Violation(models.Model):
    connectedPolicy = models.ForeignKey(ActivatedPolicy, on_delete=models.CASCADE)
    resourceName = models.CharField(max_length=200)
