import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question = models.CharField(max_length=200)
    publication_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question
    
    @admin.display(
        boolean=True,
        ordering="publication_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publication_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text