from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Like, Comment
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User



class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

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