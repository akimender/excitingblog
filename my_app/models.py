from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=450)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Comment on {self.blog.title}: {self.text} at {self.created_at}"