from django.db import models

# Create your models here.

# Create your models here.
class QuestionAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()