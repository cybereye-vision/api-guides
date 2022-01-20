from django.db import models
from django import forms
# Create your models here.
class   Question (models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()

class Choice (models.Model):
    quetion = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)


class authen_user(models.Model):
    user = models.CharField(max_length=20)
    passw = models.CharField(max_length=20)
    rule = models.IntegerField()