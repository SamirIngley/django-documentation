'''
Here, each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.
Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.

That small bit of model code gives Django a lot of information. With it, Django is able to:
Create a database schema (CREATE TABLE statements) for this app.
Create a Python database-access API for accessing Question and Choice objects.

Add polls to installed apps
'''
# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): # now when we refer to question objects, this str will return 
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text