from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views import generic
from friends.models import Friend
from django.contrib.auth import get_user_model
User = get_user_model()

def change_friends(request,operation, pk):
    user = User.objects.get(pk=pk)
    current_user = User.objects.get(pk=request.user.pk)
    if operation == 'add':
        Friend.make_friend(current_user, user)
    elif operation == 'remove':
        Friend.lose_friend(current_user, user)
    return
