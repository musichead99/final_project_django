from django.db import models
from django.core.validators import FileExtensionValidator 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    audio = models.FileField(null=True, upload_to="", blank=True, validators=[FileExtensionValidator(['mp3', 'wav', 'mid'])])
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    content = models.TextField()
    create_date = models.DateTimeField()