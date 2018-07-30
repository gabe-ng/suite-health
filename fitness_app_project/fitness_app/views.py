from django.shortcuts import render, redirect
from .models import User, Custom_Meals, Custom_Circuit
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User

############## LOG IN ############

# root page
def login_page(request):
    return render(request, 'templates/login.html', {})

############# HOMEPAGE ###########

# homepage

def homepage(request):
    return render(request, 'templates/homepage.html', {})

