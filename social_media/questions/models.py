from django.db import models
from social_media.users.models import User
# Create your models here.
from taggit.managers import TaggableManager
class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    tags = TaggableManager()
    original_question = models.ForeignKey('self',blank=True,null = True,on_delete=models.CASCADE,related_name='reposts')
    likes= models.ManyToManyField(User,related_name='question_likes',blank=True)
    answers = models.ManyToManyField(User,related_name='question_answers',through='Answer')
    repost_count = models.PositiveIntegerField(default=0)
    reposted = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    def count_question(self):
        return self.objects.all().count()

    def count_answers(self):
        return self.answers.count()
    
    def count_likes(self):
        return self.likes.count()



class Answer(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer = models.TextField()
    votes = models.ManyToManyField(User,related_name='answer_likes',blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now = True)


    def  __str__(self):
        return self.answer
    
    def count_votes(self):
        return self.votes.count()
        
    
