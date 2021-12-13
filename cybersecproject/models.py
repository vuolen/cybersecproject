from django.db import models
from django.contrib.auth.models import User

class HomePage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    welcome_message = models.TextField()