from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinis.models import Organization

class CloudiniUser(AbstractUser, models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    isManager = models.BooleanField(default=False)
    access_key = models.CharField(max_length=20)
    secret_key = models.CharField(max_length=50)
    session_token = models.CharField(max_length=400)

    class Meta:
        unique_together = ('username', 'email')

    def __str__(self):
        return self.username