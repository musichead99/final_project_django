from tkinter import CASCADE
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    audio = models.CharField(max_length=200, blank=True, default='')
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    content = models.TextField()
    create_date = models.DateTimeField()