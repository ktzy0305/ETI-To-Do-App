from django.db import models
from django.db.models import DateTimeField

# Create your models here.

class ToDoItem(models.Model):
    owner = models.CharField(max_length=100)
<<<<<<< HEAD
    Todo = models.TextField()
=======
    Todo = models.TextField()
    Timecreated = models.DateTimeField()

class ArchiveHistory(models.Model):
    owner = models.CharField(max_length=100)
    Todo = models.CharField(max_length=100)
>>>>>>> 406db8e41e9f4c4cd75a88ea58055b45a9551e8a
