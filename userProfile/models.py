from django.db import models
from django.contrib.auth.models import User

# Aesthetic
class CoverPhoto(models.Model):
    name = models.CharField(max_length=100,blank=True,default='')
    cover_photo = models.ImageField(upload_to='cover_photos/')
    def __str__(self):
        return self.name

# User Essentials
class Interest(models.Model):
    interest_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.interest_name

class PollzoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field=None)
    profile_pic = models.FileField(verbose_name=None, name=None, upload_to='profile_pic/', storage=None)
    interests = models.ManyToManyField(Interest, related_name=None, related_query_name=None, limit_choices_to=None, symmetrical=None, through=None, through_fields=None, db_constraint=True, db_table=None, swappable=True)
    desciption = models.CharField(max_length = 1000, default = '', blank=True)
    following = models.ManyToManyField('self',blank=True,symmetrical=False)
    cover_photo = models.ForeignKey(CoverPhoto,blank=True,null=True)
    def __str__(self):
        return self.user.username

class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    created_by = models.ForeignKey(PollzoUser,on_delete=models.CASCADE)
    #voted_by = models.ManyToManyField(PollzoUser,through='UserVotes')
    interests = models.ManyToManyField(Interest)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    vote_Count = models.IntegerField()

    def __str__(self):
        return self.choice_text

class UserVotes(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    voted_by_user = models.ForeignKey(PollzoUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.question.question_text +'-' +self.choice.choice_text+'-'+self.voted_by_user.user.username
