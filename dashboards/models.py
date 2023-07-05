from django.db import models

# Create your models here.

class Dashboard(models.Model):
    title = models.CharField(null=True,max_length=20)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(null=True,auto_now_add=True)
    update_at = models.DateTimeField(null=True,auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)