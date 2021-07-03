from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    #post_lists = list()
    now = datetime.now()
    #for count, post in enumerate(posts):
    #    post_lists.append("No.{}:".format(str(count)) + str(post)+ "<br>")
    #return HttpResponse(post_lists)
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
    except:
        return redirect('/')

def getTitle(request):
    url = 'http://www.pythonscraping.com/pages/page1.html'
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = str(bsObj.body.h1)
    except AttributeError as e:
        return None
    #posts = Post.objects.all()
    #print(posts, type(posts))
    #print(title, type(title))
    return render(request, 'gettitle.html', locals())
