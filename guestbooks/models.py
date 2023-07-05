from django.db import models
# Create your models here.

class Guestbook(models.Model):
    content = models.TextField()
    