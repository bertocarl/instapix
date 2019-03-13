from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

class Post(models.Model):
    user = models.ForeignKey(User)
    image = models.FileField(upload_to='user_images')
    image_url = models.CharField(max_length=255)
    caption = models.CharField(max_length=240)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    has_liked = False


    @property
    def like_count(self):
        return len(LikeModel.objects.filter(post=self))

    @property
    def comments(self):
        return CommentModel.objects.filter(post=self).order_by('created_on')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profiles_pics')
    bio = models.TextField(blank="", default="")
    name = models.CharField(max_length=255, default="", blank="")
    # phonenumber = models.IntegerField(max_length=140, blank="",default="")
    def __str__(self):
        return f'{self.user.username} Profile'


    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(Q(user__icontains=search_term) | Q(name__icontains=search_term))

        return profiles

class Followers(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.CharField(max_length=100)

class Like(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    comment_text = models.CharField(max_length=555)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save_comment(self):
        self.save()