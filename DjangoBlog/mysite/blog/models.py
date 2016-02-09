from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}".format(self.title)	


class Comment(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments")

    def __str__(self):
        return "{0}-{1}".format(self.post,self.title)


