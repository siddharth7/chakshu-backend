from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return self.user.username

class FoundPerson(models.Model):
	name = models.CharField(max_length=40, blank=True)
	location = models.CharField(max_length=40, blank=True)
	picture = models.ImageField(upload_to="static/images/products")
