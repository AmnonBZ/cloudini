from django.contrib.auth.models import AbstractUser


class CloudiniUser(AbstractUser):
    class Meta:
        unique_together = ('username', 'email')

    def __str__(self):
        return self.username