from django.db import models
from django.contrib.postgres.fields import ArrayField


class Customer(models.Model):
    name = models.CharField(max_length=200)


class Policy(models.Model):
    name = models.CharField(max_length=200)
    affectedResources = ArrayField(models.CharField(max_length=200))


class ActivatedPolicy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    metadata = ArrayField(models.CharField(max_length=200))
    actionItem = models.CharField(max_length=200)


class Violation(models.Model):
    connectedPolicy = models.ForeignKey(ActivatedPolicy, on_delete=models.CASCADE)
    resourceName = models.CharField(max_length=200)
