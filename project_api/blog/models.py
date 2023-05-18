from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/',null=True)
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    