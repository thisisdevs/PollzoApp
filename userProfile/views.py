from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import PollzoUser, Interest, CoverPhoto, Question, Choice, UserVotes
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
#from forms import QuestionForm
# Create your views here.
@login_required
def profile_view(request,user_name):
    title = user_name
    context = {
    "title":title
    }
    context["profileUser"] = user = User.objects.get(username = user_name)
    context["profile"] = profile = PollzoUser.objects.get(user=user)
    context["currentUserName"] = request.user.username
    context["followers"] = PollzoUser.objects.filter(following=profile).count()
    context["following"] = profile.following.all().count()

    if Question.objects.filter(created_by=profile).count() != 0:
        context["questions"] = questions = Question.objects.filter(created_by=profile)
        question_choices = []
        for question in questions:
            obj_to_send = {
               'question':question,
               'choices':[]
            }
            for choice in Choice.objects.filter(question = question):
                obj_to_send['choices'].append(choice)
            question_choices.append(obj_to_send)
        context['question_choices'] = question_choices
        votes_by_me = UserVotes.objects.filter(voted_by_user = PollzoUser.objects.get(user=request.user))
        my_choices = []
        for votes in votes_by_me:
            my_choices.append(votes.choice)
        context['my_choices'] = my_choices


    browsing_user = PollzoUser.objects.get(user=request.user)
    if profile in browsing_user.following.all():
        context["isFollowing"] = True
    if request.user == user:
        context["isSameUser"] = True
    return render(request,"profile/profile.html", context, content_type=None, status=None, using=None)



@login_required
def interest(request,user_name):
    context = {
    "title":"Interests",
    "all_interests":Interest.objects.all()
    }

    context["currentUser"] = request.user.first_name
    context["currentUserName"] = request.user.username
    requesting_user = get_object_or_404(User,username=user_name)
    context["currentPollzoUser"] = PollzoUser.objects.get(user=request.user)
    context["profileUser"] = requesting_user
    context["currentPollzoProfile"] = PollzoUser.objects.get(user=requesting_user)
    if request.user == requesting_user:
        context["isSameUser"] = True

    return render(request,"profile/interests.html",context)

@login_required
def followInterest(request):
    int_id = request.GET['intId']
    currentUser = PollzoUser.objects.get(user=request.user)
    interestToAdd = Interest.objects.get(pk=int_id)
    if interestToAdd in currentUser.interests.all():
        currentUser.interests.remove(interestToAdd)
        return HttpResponse(2)
    else:
        currentUser.interests.add(interestToAdd)
        return HttpResponse(1)
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('signing:initial'))
@login_required
def cover(request):
    title = "Change cover"
    context = {
        "title":title,
        "coverphotos":CoverPhoto.objects.all()
    }
    context["profileUser"] = user = request.user
    context["profile"] = profile = PollzoUser.objects.get(user=user)
    context["currentUserName"] = request.user.username
    return render(request,"profile/cover.html",context)
@login_required
def changecover(request):
    photo_id = request.GET.get("photoId",1);
    photo = CoverPhoto.objects.get(id=photo_id)
    user = PollzoUser.objects.get(user=request.user)
    user.cover_photo = photo
    user.save()
    return HttpResponse(photo.cover_photo.url)

def followuser(request):
    userid = request.GET['userId']
    userToFollow = PollzoUser.objects.get(id=userid)
    currentUser = PollzoUser.objects.get(user=request.user)
    if userToFollow in currentUser.following.all():
        currentUser.following.remove(userToFollow)
        currentUser.save()
        return HttpResponse(2)
    else:
        currentUser.following.add(userToFollow)
        currentUser.save()
        return HttpResponse(1)
@login_required
def edit(request):
    context = {
      "title":"Edit Profile"
    }
    context["currentUserName"] = request.user.username
    context['currentUser'] = user = request.user
    context['currentProfile'] = profile = PollzoUser.objects.get(user=request.user)
    if request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        desc = request.POST['desc']
        prof = None
        if request.FILES:
            prof = request.FILES['prof']
        user.first_name = fname
        if lname:
            user.last_name = lname
        if desc:
            profile.desciption = desc
        if prof:
            profile.profile_pic = prof
        user.save()
        profile.save()
        return HttpResponseRedirect(reverse('profile:userprofileview',kwargs={'user_name':user.username}))
    return render(request,"profile/edit.html",context)

@login_required
def newPoll(request):
    context = {
        "title":"Add new Poll",
        "currentUserName":request.user.username,
        "currentUser":request.user,
        "profile":PollzoUser.objects.get(user=request.user),
        "interests":Interest.objects.all(),
        "form":QuestionForm()

    }
    return render(request,"profile/new-poll.html",context)
@login_required
def newPollChoices(request):
        question_text = request.POST['question']
        interests = request.POST.getlist('int')
        if not Question.objects.filter(question_text=question_text).exists():
            new_poll = Question(question_text = question_text,created_by=PollzoUser.objects.get(user=request.user))
            new_poll.save()
            for interestId in interests:
                new_poll.interests.add(Interest.objects.get(pk=interestId))
            new_poll.save()
        else:
            new_poll = Question.objects.get(question_text=question_text)
        if 'choice_item' in request.POST:
            new_poll.choice_set.create(choice_text=request.POST['choice_item'],vote_Count=0)

        context = {
            "title":"Add new Poll",
            "currentUserName":request.user.username,
            "currentUser":request.user,
            "profile":PollzoUser.objects.get(user=request.user),
            "interests":Interest.objects.all(),
            "question":new_poll

        }
        return render(request,"profile/new-poll-choices.html",context)

def vote(request):
    qID = request.GET['qID']
    cID = request.GET['cID']
    voting_user = PollzoUser.objects.get(user=request.user)

    uVote = UserVotes(question=Question.objects.get(id=qID),choice = Choice.objects.get(id=cID),voted_by_user=voting_user)
    if uVote not in UserVotes.objects.all():
        if not UserVotes.objects.filter(voted_by_user=voting_user,question=Question.objects.get(id=qID)):
            uVote.save()
            choice_chosen = Choice.objects.get(id=cID)
            choice_chosen.vote_Count += 1
            choice_chosen.save()
            return HttpResponse(choice_chosen.vote_Count)
    return HttpResponse(0)
@login_required
def feed(request,user_name):
    if user_name != request.user.username:
        return HttpResponseRedirect(reverse('profile:feed',kwargs={'user_name':request.user.username}))
    else:
        context = {
            'title':user_name,
            'currentUserName': user_name,
            'interests':Interest.objects.all()
        }
        newsFeed = []
        currentUser = PollzoUser.objects.get(user=request.user)
        for interest in currentUser.interests.all():
            for question in Question.objects.filter(interests = interest):
                if question not in newsFeed:
                    newsFeed.append(question)
        following = currentUser.following.all()
        for user in following:
            for question in Question.objects.filter(created_by=user):
                if question not in newsFeed:
                    newsFeed.append(question)

        if len(newsFeed) != 0:
            context['newsFeed'] = newsFeed
        context['currentUser'] = currentUser
        votes_by_me = UserVotes.objects.filter(voted_by_user = PollzoUser.objects.get(user=request.user))
        my_choices = []
        for votes in votes_by_me:
            my_choices.append(votes.choice)
        context['my_choices'] = my_choices
        return render(request,'profile/newsfeed.html',context)


def deletepoll(request):
    qId = request.GET['qID']
    question = Question.objects.get(pk=qId)
    if question.created_by.user == request.user:
        question.delete()
        return HttpResponse(1)
    return HttpResponse(0)

@login_required
def following(request,user_name):
    context = {
    'message' : 'People followed by '+str(user_name),
      'title':str(user_name),
      'currentUserName':request.user.username
    }
    currentUser = User.objects.get(username=user_name)
    user = PollzoUser.objects.get(user = currentUser)
    context['user_following'] = user.following.all()
    context['i_am_following'] = PollzoUser.objects.get(user=request.user).following.all()
    return render(request,'profile/following.html',context)

@login_required
def followers(request,user_name):
    context = {
      'message' : 'People following '+str(user_name),
      'title':'People following '+str(user_name),
      'currentUserName':request.user.username
    }
    currentUser = User.objects.get(username=user_name)
    user = PollzoUser.objects.get(user = currentUser)
    context['user_following'] = PollzoUser.objects.filter(following=user)
    context['i_am_following'] = PollzoUser.objects.get(user=request.user).following.all()
    return render(request,'profile/following.html',context)

@login_required
def people(request,user_name):
    context = {
      'message' : 'All Pollzo users',
      'title':'Find People',
      'currentUserName':request.user.username
    }
    currentUser = User.objects.get(username=user_name)
    user = PollzoUser.objects.get(user = currentUser)
    all_people = []
    for p_user in PollzoUser.objects.all():
        if p_user != user:
            all_people.append(p_user)
    context['user_following'] = all_people

    context['i_am_following'] = PollzoUser.objects.get(user=request.user).following.all()
    return render(request,'profile/following.html',context)
