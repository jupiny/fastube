from django.views.generic.list import ListView

from posts.models import Post
from .base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"
