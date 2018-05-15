from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from friends.models import Friend
class TestPage(TemplateView):
    template_name = 'test.html'

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
            args ={'friends': friends}
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
