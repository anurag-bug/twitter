from django import forms
from django.forms import ModelForm
from . import models


class SearchForm(ModelForm):
    class Meta:
        model=models.tweetModel
        fields = ['term','number']
        labels = {
            "term": "Keyword",
            "number": "No. of Tweets"
        }

