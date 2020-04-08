from django.db import models
from django.contrib.auth.models import AbstractUser


class Custom_User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    display_name = models.CharField(max_length=80)

