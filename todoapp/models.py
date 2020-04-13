from django.db import models

# Create your models here.
class TodoItem(models.Model):
   content = models.TextField()
   deadline = models.DateField(default= "2025-12-31")
