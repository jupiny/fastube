from django.conf.urls import url

from posts.api import *


urlpatterns = [
    url(r'^posts/$', PostListAPIView.as_view(), name="posts"),
    url(r'^(?P<slug>\w+)/comments/$', PostCommentsListAPIView.as_view(), name="comments"),
]
