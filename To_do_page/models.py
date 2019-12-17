from django.db import models
from django.db.models import DateTimeField

# Create your models here.

class ToDoItem(models.Model):
    owner = models.CharField(max_length=100)

    Todo = models.TextField()

    Timecreated = models.DateTimeField()

class ArchiveHistory(models.Model):
    owner = models.CharField(max_length=100)
    Todo = models.CharField(max_length=100)

