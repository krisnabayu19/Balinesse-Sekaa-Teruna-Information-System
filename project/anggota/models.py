from distutils.command.upload import upload
from email.policy import default
import os
from random import random
from django.db import models
from django.dispatch import receiver
import datetime

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

# Create your models here.
class UserProfileModel(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'auth_user'

        
