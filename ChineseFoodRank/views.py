#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.views.generic import ListView
from django.shortcuts import render_to_response
from ChineseFoodRank.models import Category,Food,Link,Vote,Style
from ChineseFoodRank.forms import CategoryForm,UserForm,UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.base import ContentFile

def index(request):
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    context_dict = {
        'category_list':category_list,
         'style_list':style_list
    }
    return render(request,'index.html', context_dict)

def register(request):
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                 profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    context_dict = {
        'category_list':category_list,
         'style_list':style_list,
         'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    # Render the template depending on the context.
    return render(request, 'register.html',context_dict)

def user_login(request):
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    context_dict = {
        'category_list':category_list,
         'style_list':style_list
    }
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('../',context_dict)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'error.html', context_dict)


    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', context_dict)

def rank(request):
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    foods_Top3 = Food.objects.order_by('-likes')[0:3]
    foods_Top10 = Food.objects.order_by('-likes')[3:14]
    context_dict = {
        'foods_Top3': foods_Top3,
        'foods_Top10': foods_Top10,
         'category_list':category_list,
         'style_list':style_list
    }
    return render(request, 'rank.html', context_dict)

def about(request):
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    context_dict = {
        'category_list':category_list,
         'style_list':style_list
    }
    return render(request, 'about.html',context_dict)

def error(request):
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    context_dict = {
        'category_list':category_list,
         'style_list':style_list
    }
    return render(request, 'error.html',context_dict)


def food(request, foodid):
    food = Food.objects.get(foodid=foodid)
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    print (food)
    context_dict = {
        'food':food,
         'category_list':category_list,
         'style_list':style_list
    }
    return render(request, 'food.html', context_dict)

def searchfood(request):
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    searchfood = request.GET['searchfood']
    print searchfood
    result_list = Food.objects.filter(title__icontains=searchfood).order_by('-likes')[0:10]    #include the name
    for a in result_list:
            print "- {0}".format(str(a))
    context_dict = {
        'category_list':category_list,
        'style_list':style_list,
        'result_list' : result_list
    }
    # {% for food in result_list %}
    return render(request,"searchlist.html", context_dict)



def searchandrank(request):
    category_list = Category.objects.all()
    style_list = Style.objects.all()
    searchstyle = request.GET['searchstyle']
    serachcategory = request.GET['serachcategory']
    print searchstyle
    print serachcategory

    if  serachcategory!='0':
        result_list = Food.objects.filter(category__name=serachcategory).order_by('-likes')[0:10]    #include the name
    if  searchstyle!='0':
        result_list = Food.objects.filter(style__name=searchstyle).order_by('-likes')[0:10]    #include the name
    if serachcategory != '0'and searchstyle!='0':
        result_list = Food.objects.filter(style__name=searchstyle,category__name=serachcategory).order_by('-likes')[0:10]    #include the name


   # result_list = Food.objects.filter(category__name=serachcategory).order_by('-likes')[0:10]    #include the name
    for a in result_list:
            print "- {0}".format(str(a))
    context_dict = {
        'category_list':category_list,
        'style_list':style_list,
        'result_list' : result_list
    }
    # {% for food in result_list %}
    return render(request,"searchlist.html", context_dict)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('../')

def commodity_list(request):
	commodities = Category.objects.all()
	categories = Category.objects.all()
	username = request.user.username
	if request.user.is_authenticated():
		return render_to_response("commoditiy_list.html",RequestContext(request,{"commodities": commodities,"categories":categories,"logged":True,"username":username,}))
	else:
		return render_to_response("commoditiy_list.html",RequestContext(request,{"commodities": commodities,"categories":categories,"logged":False}))