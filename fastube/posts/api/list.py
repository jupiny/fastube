from django.http.response import HttpResponse

from rest_framework.generics import ListAPIView

from posts.models import Post
from posts.serializers import PostModelSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
