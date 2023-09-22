from django.db import models

class Question(models.Model):
    headline = models.CharField(max_length=100)
    lead = models.TextField()
    invest = models.CharField(max_length=30)
    answer = models.BooleanField()
