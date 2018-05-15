from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'friends'

urlpatterns = [
    url(r"(?P<operation>.+)/(?P<pk>\d+)/$",views.change_friends,name="change_friends"),
]
