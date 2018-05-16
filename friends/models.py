from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='friends', null=True,on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = Friend.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)
        friend.save()

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = Friend.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)
        friend.save()
