from django.shortcuts import render, redirect
# from .models import User
# from .models import User, Custom_Meals, Custom_Circuit
# from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests
import json
from django.contrib.auth.models import User
from pprint import pprint


def landing(request):
    return render(request, "fitness_app/landing.html", {})


def index(request):
    return render(request, "fitness_app/index.html", {})


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "fitness_app/profile.html", {"username": username})


############## LOG IN ############

# root page
def login_view(request):
    if request.method == "POST":
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/index")
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, "fitness_app/login.html", {"form": form})


def signup_view(request):
    # POST Request for a new user
    if request.method == 'POST':
        # Verify passwords
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                # If Username already exists, render form with error
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'fitness_app/signup.html', {'error': 'Username already in use'})
            # If user does not exist, create and login new user then redirect to home
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('/index')
        else:
            return render(request, 'fitness_app/signup.html', {'error': 'Passwords do not match'})
    # GET request for empty sign up form
    else:
        return render(request, 'fitness_app/signup.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/index")


############# HOMEPAGE ###########

# homepage


def homepage(request):
    return render(request, "fitness_app/homepage.html")


############# PROFILE ###########

# profile


def dashboard(request, username):
    return render(request, 'fitness_app/dashboard.html')


################ WORKOUT API ############

# GET

def find_workout(request, limit):
    print('in views',limit)
    url = 'https://wger.de/api/v2/exercise/?limit='+ limit
    r = requests.get(url=url)
    return HttpResponse(r, content_type='application/json')

# POST

def save_workout(request):
    print("placeholder")

################ FOOD API ############


def find_food(request):
    r = requests.get("https://wger.de/api/v2/exercise/?limit=1")
    r.content
