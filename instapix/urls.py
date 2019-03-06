from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views 
from django.conf.urls.static import static


urlpatterns=[
   url(r'^accounts/', include('registration.backends.simple.urls')),
   url(r'^logout/$', views.logout, {"next_page": '/'}),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)