from django.shortcuts import render
from mysite import models
# Create your views here.


def index(request):
    products = models.Products.objects.all()
    return render(request, 'index.html', locals())


def detail(request, id):
    try:
        product = models.Products.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    return render(request, 'detail.html', locals())
