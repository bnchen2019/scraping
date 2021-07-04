from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Product
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

def listing(request):
    products = Product.objects.all()	
    return render(request, 'list.html', locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    return render(request, 'disp.html', locals())

def index(request, tvno = 0):
    tv_list = [{'name':'民視', 'tvcode':'XxJKnDLYZz4'},
			{'name':'MUSIC', 'tvcode':'o4PfZFOSwbY'},
			{'name':'KKBOX', 'tvcode':'hXg6jQ5Ea_Q'},
			{'name':'華視', 'tvcode':'g9uJqP0hT_I'},
			{'name':'中天', 'tvcode':'hgIfZz8STLk'},]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'indextv.html', locals())

def carlist(request, maker=0):
	car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
	car_list = [ [],
			['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
			['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
			['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
			['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
			['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
			  ]
	maker = maker
	maker_name =  car_maker[maker]
	cars = car_list[maker]
	return render(request, 'carlist.html', locals())

