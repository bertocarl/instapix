from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.home,name='home'),
    url('^new/post$',views.new_post, name='new-post'),
    url('^search/',views.search_results,name='search_results'),
    url('^search/',views.search_results,name='search_results'),
    url('^new/post$',views.new_post, name='new-post'),
    url('^new/location$',views.new_location, name='new-location'),
    url('^profile/',views.profile, name='profile'),
    url('^edit/profile$',views.edit_profile, name='edit-profile'),
    url('^explore/',views.explore, name='explore'),
    url('^like/$', views.like, name='like'),
    # url('^register/', views.register, name='register'),
    url('^search/',views.search_results, name='search_results'),
    url('^user-profile/(\d+)',views.userprofile,name='user-profile'),
    url('^comment/$',views.comment,name='comment'),
    url('^change_profile/(?P<username>\w{0,50})',views.change_profile,name='change_profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
