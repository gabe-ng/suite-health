from django.shortcuts import render, redirect
# from .models import User, Custom_Meals, Custom_Circuit
# from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User


############## LOG IN ############

# root page
def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request, username):
    return render(request, 'profile.html')


############# HOMEPAGE ###########

# homepage

def homepage(request):
    return render(request, 'templates/homepage.html')

############# PROFILE ###########

# profile

def dashboard(request):
    return render(request, 'templates/dashboard.html', {})
