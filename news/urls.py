from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
   
    url('^$',views.welcome,name = 'welcome'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^village/', views.village, name='village'),
    url(r'^business/', views.business, name='business'),
    url(r'^police/', views.police, name='police'),
    url(r'^health/', views.health, name='health'),
    url(r'^search_results/', views.search_results, name='search_results'),

    url(r'^myProfile/(\d+)', views.myProfile, name='myProfile'),
    url(r'^myVillage/(\d+)', views.myVillage, name='myVillage'),
     # url(r'^comments/', views.comments, name='comments'),
    url(r'^post$',views.post,name ='post'),
    url(r'^posts/(\d+)',views.posts,name ='posts'),
    url(r'^guest/', views.guest, name='guest'),


   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)