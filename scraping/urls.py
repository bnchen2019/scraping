"""scraping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views import index, detail
from mysite8.views import index2, listing, posting, contact, post2db

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index2),
    path('<int:pid>/<str:del_pass>', index2),
    path('list/', listing),
    path('post/', posting),
    path('contact/', contact),
    path('post2db/', post2db),
    path('detail/<int:id>', detail, name = 'detail-url'),
]
