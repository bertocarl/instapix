from django.conf.urls import url,include
from django.conf import settings
from django.contrib.auth import views 
from django.shortcuts import render
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url(r'', views.home),
    url(r'^sign-up$', views.signup),
   ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 