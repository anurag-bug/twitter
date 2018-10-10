from django.db import models

# Create your models here.
class tweetModel(models.Model):
    term = models.TextField(max_length=100, null=False)
    number = models.IntegerField(null=False)