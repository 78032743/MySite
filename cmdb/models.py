from django.db import models


# Create your models here.
class MovieInfo(models.Model):
    ranking = models.CharField(max_length=3, default="", primary_key=True)
    title = models.CharField(max_length=20, default="")
    personnel_info = models.CharField(max_length=50, default="")
    year = models.CharField(max_length=4, default="")
    country = models.CharField(max_length=10, default="")
    type = models.CharField(max_length=40, default="")
    score = models.CharField(max_length=4, default="")
    num = models.CharField(max_length=20, default="")


class JDGoodsInfo(models.Model):
    title = models.CharField(max_length=50, default="", primary_key=True)
    price = models.URLField(max_length=10, default="")
    commit = models.URLField(max_length=10, default="")
