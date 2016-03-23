from django.conf.urls import patterns, url, include
from  django.contrib import admin
import ChineseFoodRank

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', ChineseFoodRank.index, name='index'),
)