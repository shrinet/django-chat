from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    label = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    category = models.CharField(max_length=50)
    question = models.TextField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer