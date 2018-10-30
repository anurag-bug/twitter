from django.db import models

# Create your models here.
class tweetModel(models.Model):
    term = models.TextField(max_length=100, null=False)
    number = models.IntegerField(null=False)

class positiveTweets(models.Model):
    tweetText = models.TextField(max_length=300,null=False)
    userName = models.TextField(max_length=20,null=True)
    time = models.TextField(max_length=10)

class negativeTweets(models.Model):
    tweetText = models.TextField(max_length=300,null=False)
    userName = models.TextField(max_length=20,null=True)
    time = models.TextField(max_length=10,null=True)