from django.shortcuts import render, redirect
from .models import Custom_Meal, Custom_Circuit
# from django.contrib.auth.decorators import login_required
# from .forms import LoginForm, SignupForm
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests
import json
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def landing(request):
    return render(request, "fitness_app/landing.html", {})

def about(request):
    return render(request, "fitness_app/about.html", {})


def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "fitness_app/profile.html", {"username": username})

## create ##

def circuitForm(request):
    if request.method == "POST":
        # name = request.POST["name"]
        # workouts = request.POST["workouts"]
        user = request.user
        if user.is_active:
            circuit = Custom_Circuit.objects.create(user=user, name=request.POST["name"], workouts=request.POST["workouts"])
            # return HttpResponseRedirect("/homepage")
            return redirect('dashboard', username = user.username)
        else:
            return render(request, 'fitness_app/circuits.html', {'error': "please login"})
    else:
        return render(request, "fitness_app/circuits.html")

def mealForm(request):
    if request.method == "POST":
        # name = request.POST["name"]
        # workouts = request.POST["workouts"]
        user = request.user
        if user.is_active:
            meal = Custom_Meal.objects.create(user=user, label=request.POST["label"], ingredients=request.POST["ingredients"], instructions=request.POST["instructions"], portions=request.POST["portions"], macros=request.POST["macros"])
            # return HttpResponseRedirect("/homepage")
            return redirect('dashboard', username = user.username)
        else:
            return render(request, 'fitness_app/meals.html', {'error': "please login"})
    else:
        return render(request, "fitness_app/meals.html")


############## LOG IN ############

# root page
def login_view(request):
    if request.method == "POST":
        # if post, then authenticate (user submitted username and password)
        if request.POST['username'] != "" and request.POST['password'] != "":
            u = request.POST["username"]
            p = request.POST["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/homepage")
                else:
                    return render(request, 'fitness_app/login.html', {'error': "The account has been disabled."})
            else:
                return render(request, 'fitness_app/login.html', {'error': "The username and/or password is incorrect."})
    else:
        return render(request, "fitness_app/login.html")

def signup_view(request):
    # POST Request for a new user
    if request.method == 'POST':
        # Verify passwords
        if request.POST['password'] == request.POST['confirm_password'] and request.POST['password'] != "":
            try:
                # If Username already exists, render form with error
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'fitness_app/signup.html', {'error': 'Username already in use'})
            # If user does not exist, create and login new user then redirect to home
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('/homepage')
        else:
            return render(request, 'fitness_app/signup.html', {'error': 'Passwords do not match'})
    # GET request for empty sign up form
    else:
        return render(request, 'fitness_app/signup.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/homepage")


############# HOMEPAGE ###########

# homepage

def homepage(request):
    return render(request, "fitness_app/homepage.html")

def custom_meals(request):
    meals = Custom_Meal.objects.all()
    data = serializers.serialize('json', meals)
    return JsonResponse({ 'meals': data })

def custom_circuits(request):
    circuits = Custom_Circuit.objects.all()
    data = serializers.serialize('json', circuits)
    return JsonResponse({ 'circuits': data })


############# PROFILE ###########

# profile

def dashboard(request, username):
    circuits = Custom_Circuit.objects.filter(user=request.user)
    meals = Custom_Meal.objects.filter(user=request.user)
    return render(request, 'fitness_app/dashboard.html', {'circuits':circuits, 'meals':meals})

################ WORKOUT API ############

# GET

def find_workout(request, muscle):
    url = 'https://wger.de/api/v2/exercise/?language=2&muscles=' + muscle
    r = requests.get(url=url)
    return HttpResponse(r, content_type='application/json')

# POST
@csrf_exempt
def save_workout(request, data):
    r = requests.post(url='http://localhost:8000/homepage/', data = data)
    console.log('workout saved from SAVE_WORKOUT function in views')


################ FOOD API ############
def find_food(request, food):
    print(food)
    url = 'https://api.edamam.com/api/food-database/parser?ingr='+ food + '&app_id=2d7d9644&app_key=8e911eeff3b68f04eafd1fffeaf16401'
    r = requests.get(url=url)
    return HttpResponse(r, content_type='application/json')
