from django.contrib import admin
from .models import PollzoUser, Interest, CoverPhoto, Question, Choice, UserVotes
# Register your models here.
admin.site.register(PollzoUser, admin_class=None)
admin.site.register(Interest, admin_class=None)
admin.site.register(CoverPhoto, admin_class=None)
admin.site.register(Question, admin_class=None)
admin.site.register(Choice, admin_class=None)
admin.site.register(UserVotes, admin_class=None)
