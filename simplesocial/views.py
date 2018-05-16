from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from friends.models import Friend
from posts.models import Post
from groups.models import Group

from django.http import HttpResponse
import json

from django.contrib.auth import get_user_model
User = get_user_model()

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                friend = Friend.objects.get(current_user=request.user)
                friends = friend.users.all()

            except Friend.DoesNotExist:
                friends = []
            try:
                users = User.objects.all()
                noFriends =[]
                for user in users:
                    if user in friends:
                        pass
                    else:
                        noFriends.append(user)
            except:
                noFriends=[]
            return render(request,"index.html",{'friends':friends,'nofriends':noFriends})
        return super().get(request, *args, **kwargs)
class usersjson(TemplateView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        jsonArr =[]
        for user in users:
            jsonResponse = {}
            jsonResponse['user_id']=user.id
            jsonResponse['user_name']=user.username
            jsonResponse['user_email']=user.email
            jsonResponse['user_first_name']=user.first_name
            jsonResponse['user_last_name']=user.last_name

            jsonArr.append(jsonResponse)
        return HttpResponse(json.dumps(jsonArr), content_type="application/json")
class postsjson(TemplateView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        jsonArr =[]
        for post in posts:
            jsonResponse = {}
            user = post.user
            jsonResponse['user_name']=user.username
            jsonResponse['post_text']=post.message
            jsonResponse['post_group']=post.group.name

            jsonArr.append(jsonResponse)
        return HttpResponse(json.dumps(jsonArr), content_type="application/json")
class groupsjson(TemplateView):
    def get(self, request, *args, **kwargs):
        groups = Group.objects.all()
        posts = Post.objects.all()
        jsonArr =[]
        postsArr=[]
        membersArr=[]
        for group in groups:
            groupResponse={}
            groupResponse['group_name']=group.name
            groupResponse['group_description']=group.slug
            for post in group.posts.all():
                jsonResponse = {}
                user = post.user
                jsonResponse['user_name']=user.username
                jsonResponse['post_text']=post.message
                postsArr.append(jsonResponse)
            #Needs fixing
            # members = group.members.filter(group=group)
            # if(members):
            #     for groupMember in members:
            #         memberResponse = {}
            #         memberResponse['user_name']=groupMember.username
            #         membersArr.append(memberResponse)
            #     groupResponse['group_members']=membersArr
            jsonArr.append(groupResponse)
        return HttpResponse(json.dumps(jsonArr), content_type="application/json")
