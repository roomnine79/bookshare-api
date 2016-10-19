
from django.db import models 
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    sex = models.CharField(max_length=50,default='Male')
    birthday = models.DateField()
    user = models.OneToOneField(User,primary_key=True,related_name='profile')
    nickname = models.CharField(max_length=100,blank=True)

