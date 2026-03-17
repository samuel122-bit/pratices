from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255, unique=True)
    option1 =models.CharField(max_length=100)
    option2 =models.CharField(max_length=100)
    option3 =models.CharField(max_length=100)
    option4 =models.CharField(max_length=100)
    correct = models.IntegerField()

    def __str__(self):
        return self.text
    
class Score(models.Model):
    username = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return self.username