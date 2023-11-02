from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation
from social_media.users.models import User 
# Tag Manager Package 
from taggit.managers import TaggableManager

# Hitcount to count the views
from hitcount.models import HitCountMixin,HitCount

# class Author(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='authors') # to access the Auther model from user model

#     def __str__(self):
#         return self.user.username

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body= models.TextField()
    image = models.ImageField(blank=True,null=True,upload_to='blog_images/')
    tags= TaggableManager()
    # Hit count filed 
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_p',
        related_query_name='hit_count_generic_relation')
    comments = models.ManyToManyField(User,related_name='blog_comments',through='Comment')
    likes = models.ManyToManyField(User,related_name='blog_likes',blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()
    
    def comments_count(self):
        return self.comments.count()
    
class Comment(models.Model):
    comment= models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    blog= models.ForeignKey(Blog,on_delete= models.CASCADE)
    comment_pub_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} by {self.user.username}"



