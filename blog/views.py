from django.shortcuts import render
from django.utils import timezone
from .models import Post                # we decide to display the Post model

# A view...
# takes a Web request and returns a Web response
# Here we decide...
# what models to display in a template

# Create your views here.

def post_list(request):
    # create an object "posts" of all posts containing "post" in title
    posts = Post.objects.filter(title__contains="post")
    # render/put together the template 'blog/post_list.html'
    # create HTML tag for the posts object and call it "posts" (green below)
    return render(request, 'blog/post_list.html', {'posts': posts})

# Each HTML is divided into two elements:
# <head> (information about the document that is not displayed on the screen)
# <body> (everything else that is displayed as part of the web page)

# 1) (views.py) create object "posts" in post_list function
# 2) (post_list.html) add {{ post }} to HTML
# 3) run server
# 4) reload site