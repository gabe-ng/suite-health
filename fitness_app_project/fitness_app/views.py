from django.shortcuts import render, redirect
from .models import User, Custom_Meal, Custom_Circuit
from django.contrib.auth.decorators import login_required
import requests

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User

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
                    return HttpResponseRedirect("/")
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})


############# HOMEPAGE ###########

# homepage


def homepage(request):
    return render(request, "fitness-app/homepage.html", {})


# add urls
# homepage.js call view endpoint
def food_view(request):
    # id = request.id
    # food = Food.objects.get(id=id)
    # if request.method == "POST":
    #     r = requests.get(
    #         "https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id=2d7d9644&app_key=8e911eeff3b68f04eafd1fffeaf16401",
    #         params=request.POST,
    #     )
    # else:
    #     r = requests.get(
    #         "https://api.edamam.com/api/food-database/parser?ingr=steak&app_id=2d7d9644&app_key=8e911eeff3b68f04eafd1fffeaf16401",
    #         params=request.GET,
    #     )

    r = requests.get(
        "https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id=2d7d9644&app_key=8e911eeff3b68f04eafd1fffeaf16401"
    )

    if r.status_code == 200:
        return render(request, "fitness-app/homepage.html", {})
    return print("error")


############## PROFILE ##############
