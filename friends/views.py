from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from friends.models import Friend
from django.contrib.auth import get_user_model
User = get_user_model()

def change_friends(request,operation, pk,home):
    user = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, user)
    elif operation == 'remove':
        Friend.lose_friend(request.user, user)
    if(home=='no'):
        return HttpResponseRedirect("/posts/by/{}".format(user.username))
    else:
        return HttpResponseRedirect("/")
