from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings# New Import
from django.conf.urls.static import static # New Import
from ChineseFoodRank.models import Category
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'ChineseFoodRank.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'ChineseFoodRank.views.register', name= 'register'),
    url(r'^login/$', 'ChineseFoodRank.views.user_login', name='login'),
    url(r'^logout/$', 'ChineseFoodRank.views.user_logout', name='logout'),
    url(r'^rank/', 'ChineseFoodRank.views.rank', name='rank'),
    url(r'^about/', 'ChineseFoodRank.views.about', name='about'),
    url(r'^error/', 'ChineseFoodRank.views.error', name='error'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
    url(r'^searchfood/', 'ChineseFoodRank.views.searchfood', name='searchfood'),
    url(r'^searchandrank/', 'ChineseFoodRank.views.searchandrank', name='searchandrank'),
    url(r'^searchlist/', 'ChineseFoodRank.views.searchandrank', name='searchlist'),

    url(r'^food/(?P<foodid>[\w\-]+)/$', 'ChineseFoodRank.views.food',name='foodid'),


)+static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)