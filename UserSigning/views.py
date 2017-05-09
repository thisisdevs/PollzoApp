from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from userProfile.models import PollzoUser
# Create your views here.
def initialRedirection(request):
    return HttpResponseRedirect(reverse('signing:login'))


def login_view(request):
    title = 'pollzo'
    context = {
      "title":title
    }
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profile:userprofileview',kwargs={'user_name':request.user.username}))
    if request.POST:
        user_name = request.POST['user_name']
        pass_word = request.POST['pass_word']
        user = authenticate(username=user_name,password=pass_word)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('profile:userprofileview',kwargs={'user_name':request.user.username}))
        else:
            context['message'] = 'Invalid Credentials'
    return render(request,"signing/login.html", context, content_type=None, status=None, using=None)

def signup_view(request):
    title = 'SignUp'
    context = {
      'title':title
    }
    if request.POST:
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        pass_word = request.POST['pass_word']
        profile_pic = request.FILES['prof']

        if User.objects.filter(username=user_name).exists():
            context["message"] = "User already exists with this username!"
        else:
            new_user = User.objects.create_user(user_name, email=email, password=pass_word)
            new_user.first_name = first_name
            new_user.save()
            new_user_profile = PollzoUser(user=new_user,profile_pic=profile_pic)
            new_user_profile.save(force_insert=False, force_update=False, using=None, update_fields=None)
            login(request, new_user, backend=None)
            return HttpResponseRedirect(reverse('profile:userprofileview',kwargs={'username':user_name}))
    return render(request,"signing/signup.html", context, content_type=None, status=None, using=None)
