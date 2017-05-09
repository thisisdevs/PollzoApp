from django.conf.urls import url
from . import views

app_name = 'profile'

urlpatterns=[
   url(r'^(?P<user_name>[a-z]+)/$', views.profile_view, kwargs=None, name='userprofileview'),
   url(r'^(?P<user_name>[a-z]+)/interests/$',views.interest,name='interests'),
   url(r'^(?P<user_name>[a-z]+)/newsfeed/$',views.feed,name='feed'),
   url(r'^(?P<user_name>[a-z]+)/following/$',views.following,name='following'),
   url(r'^(?P<user_name>[a-z]+)/followers/$',views.followers,name='followers'),
   url(r'^(?P<user_name>[a-z]+)/people/$',views.people,name='people'),
   url(r'^logout',views.logout_view,name='logout'),
   url(r'^ajaxrequest/followinterest/$',views.followInterest),
   url(r'^ajaxrequest/changecover/$',views.changecover),
   url(r'^ajaxrequest/followuser/$',views.followuser),
   url(r'^ajaxrequest/vote/$',views.vote),
   url(r'^ajaxrequest/delete/$',views.deletepoll),
   url(r'^editprofile/cover/$',views.cover,name='cover'),
   url(r'^editprofile/profile/$',views.edit,name='edit'),
   url(r'^new-poll/add/$',views.newPoll,name='new-poll'),
   url(r'^new-poll/add-choices/$',views.newPollChoices,name='new-poll-choices'),
]
