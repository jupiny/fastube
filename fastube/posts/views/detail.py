from django.views.generic.detail import DetailView

from posts.models import Post
from .base import PostBaseView


class PostDetailView(PostBaseView, DetailView):
    template_name = "posts/detail.html"
    slug_field = "hash_id"
