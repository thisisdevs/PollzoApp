from django.conf.urls import url
from . import views
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.conf.urls.static import static

app_name = 'signing'

urlpatterns = [
   url(r'^$', views.initialRedirection, kwargs=None, name='initial'),
   url(r'^login/$', views.login_view, kwargs=None, name='login'),
   url(r'^register/$', views.signup_view, kwargs=None, name='signup')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
