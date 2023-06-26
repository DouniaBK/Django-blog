from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView): # code for posts list in the blog
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6  # the number of posts on the page is set to 6
    # django will automatically create a second page for post number 7 and on