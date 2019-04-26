from django.contrib import admin
from .models import *


# Register your models here.
class MovieInfoAdmin(admin.ModelAdmin):
    list_display = ('ranking', 'title', 'personnel_info', 'year', 'country', 'type', 'score', 'num')


class JDGoodsInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'commit')


admin.site.register(MovieInfo, MovieInfoAdmin)
admin.site.register(JDGoodsInfo, JDGoodsInfoAdmin)
