from django.shortcuts import render
from cmdb import models
from crawler.dynamic_crawler import dynamic_crawler_main
from crawler.static_crawler import static_crawler_main


# Create your views here.

def index(request):
    return render(request, 'index.html')


def top250(request):
    static_crawler_main()
    movie_list = models.MovieInfo.objects.all()
    return render(request, 'top250.html', {"movie_list": movie_list})


def jdgoods(request):
    dynamic_crawler_main()
    goods_list = models.JDGoodsInfo.objects.all()
    return render(request, 'jdgoods.html', {"goods_list": goods_list})
