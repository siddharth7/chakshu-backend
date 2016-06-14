from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)

    def __unicode__(self):
        return self.user.username