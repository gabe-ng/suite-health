from django.shortcuts import render, redirect
from .models import User, Custom_Meals, Custom_Circuit
from django.contrib.auth.decorators import login_required

############## LOG IN ############

# root page
def login_page(request):
    return render(request, 'templates/login.html', {})

############# HOMEPAGE ###########

# homepage

def homepage(request):
    return render(request, 'templates/homepage.html', {})

############# PROFILE ###########

# dashboard

def dashboard(request):
    return render(request, 'templates/dashboard.html', {})
