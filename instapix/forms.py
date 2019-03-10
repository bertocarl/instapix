from django import forms
from .models import User, Post, Like, Comment
from django.contrib.auth import authenticate, login, logout, get_user_model


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['image', 'caption']


class LikeForm(forms.ModelForm):

    class Meta:
        model = Like
        fields=['post']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_text', 'post']