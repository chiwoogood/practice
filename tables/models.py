from django.db import models

# Create your models here.
class Table(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    crated_at = models.DateTimeField(null=True,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

