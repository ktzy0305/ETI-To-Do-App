from django.db import models

# Create your models here.

class ToDoItem(models.Model):
    owner = models.CharField(max_length=100)
    Todo = models.TextField()

class ArchiveHistory(models.Model):
    owner = models.CharField(max_length=100)
    Todo = models.CharField(max_length=100)