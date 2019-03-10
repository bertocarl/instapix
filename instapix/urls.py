from django.conf.urls import url,include
from django.conf import settings
from django.contrib.auth import views 
from django.shortcuts import render
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'', views.login_view),
    url(r'^signup/', views.signup_view),
    url(r'^feeds/', views.feed_view),
    url(r'^post/', views.post_view),
   ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 