from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Category(models.Model):                                       #every class like a table
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True)
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Food(models.Model):
    foodid= models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, null=True)
    style = models.ForeignKey(Style, null=True)
    likes = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    url = models.URLField(null=True)
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title


class FoodAdmin(admin.ModelAdmin):
    list_display = ('title','likes','category','style')

class Link(models.Model):
    title = models.CharField("headline", max_length=100)
    submitter = models.ForeignKey(User)
    submitter_on = models.DateTimeField(auto_now_add= True)
    rank_score = models.FloatField(default=0.0)
    url = models.URLField("URL", max_length=250, blank= True)
    description = models.TextField(blank=True)
    def __unicode__(self):
        return self.title

class Vote(models.Model):
    voter = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    def __unicode__(self):
        return "%s voted %s" % (self.voter.username, self.food.foodid)



