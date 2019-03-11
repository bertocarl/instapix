from django.conf.urls import url,include
from django.conf import settings
from django.contrib.auth import views 
from django.shortcuts import render
from django.conf.urls.static import static
from . import views
from .models import Post
# from django.urls import path

urlpatterns=[
    
    url(r'^post/', views.post_view),
    url(r'^register/', views.register, name='register'),
    
   ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 