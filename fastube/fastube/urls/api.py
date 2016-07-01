from django.conf.urls import url

from posts.api import *


urlpatterns = [
    url(r'^posts/$', PostListAPIView.as_view(), name="posts"),
    url(r'^posts/(?P<slug>\w+)/comments/$', PostCommentsListCreateAPIView.as_view(), name="comments"),
]
