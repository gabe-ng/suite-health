from django.shortcuts import render
# from .models import User
# from .models import User, Custom_Meals, Custom_Circuit
# from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', {})

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'username': username})


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
        return render(request, 'fitness_app/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    # print("The account has been disabled.")
                    HttpResponse("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    # logout(request)
    return HttpResponseRedirect('/')


############# HOMEPAGE ###########

# homepage

def homepage(request):
    return render(request, 'fitness_app/homepage.html')

############# PROFILE ###########

# profile

def dashboard(request, username):
    return render(request, 'fitness_app/dashboard.html')
