from django.shortcuts import render

# A view:
# takes a Web request and returns a Web response

# Create your views here.

def post_list(request):
    # render/put together the template 'blog/post_list.html'
    return render(request, 'blog/post_list.html', {})

# Each HTML is divided into two elements:
# <head> (information about the document that is not displayed on the screen)
# <body> (everything else that is displayed as part of the web page)