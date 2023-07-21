from django.contrib.auth.models import User, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    is_active = models.BooleanField(default=False)


class Location(models.Model):
    u = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    time_added = models.DateTimeField(auto_now_add=True)
