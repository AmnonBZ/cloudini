from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Organization(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    main_user_password = models.CharField(max_length=32)

    class Meta:
        unique_together = ('name', 'email')

    def save(self, *args, **kwargs):
        super(Organization, self).save(*args, **kwargs)
        CloudiniUser.objects.create(username=self.name, email=self.email, is_active=False,
                                    password=self.main_user_password,
                                    organization=Organization.objects.get(name=self.name))


class CloudiniUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    password = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('username', 'email')

    def save(self, *args, **kwargs):
        user = User.objects.create_user(username=self.username, password=self.password, email=self.email,
                                        is_staff=False, is_superuser=False, is_active=self.is_active)
        user.save()

        super(CloudiniUser, self).save(*args, **kwargs)


class Policy(models.Model):
    name = models.CharField(max_length=200)
    affectedResources = ArrayField(models.CharField(max_length=200))


class ActivatedPolicy(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    metadata = ArrayField(models.CharField(max_length=200))
    actionItem = models.CharField(max_length=200)


class Violation(models.Model):
    connectedPolicy = models.ForeignKey(ActivatedPolicy, on_delete=models.CASCADE)
    resourceName = models.CharField(max_length=200)
