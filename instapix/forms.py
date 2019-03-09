from django import forms
from .models import User, PostModel, LikeModel, CommentModel
from django.contrib.auth import authenticate, login, logout, get_user_model


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['email','username','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['image', 'caption']


class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']