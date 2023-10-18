from django.db import models
from django.contrib.auth.models import AbstractUser


from social_media.users.models import User 
class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='authors') # to access the Auther model from user model

    def __str__(self):
        return self.user.username
    
class Blog(models.Model):
    title = models.CharField(max_length=128)
    body= models.TextField()
    tags= models.CharField(max_length=128)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    comments = models.ManyToManyField(User,related_name='blog_comments',through='Comment')
    likes = models.ManyToManyField(User,related_name='blog_likes',blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment= models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    Blog= models.ForeignKey(Blog,on_delete= models.CASCADE)
    comment_pub_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} by {self.user.username}"




