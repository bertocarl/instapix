from django.db import models

class User(models.Model):
    is_authenticated = True
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=140)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(auto_now=True)
    proflepic = models.CharField(max_length=255, default="")

