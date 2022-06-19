from django.contrib.auth import get_user_model
##from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
User = get_user_model()
# Create your models here.
class Post(models.Model):
    Text = models.TextField()
    Author = get_user_model()
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self
 

