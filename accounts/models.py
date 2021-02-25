from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User Model
class CustomUser(AbstractUser):
    displayname = models.CharField(max_length=50, null=True, blank=True)
    homepage = models.URLField(null=True, blank=True)

    # Add REQUIRED_FIELDS so fields will prompt on createsuperuser
    REQUIRED_FIELDS = ['displayname', 'homepage']

    def __str__(self):
        return f'{self.username} {self.id} | {self.password} | {self.displayname} | {self.homepage}'
