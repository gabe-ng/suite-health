from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    ############## LOG IN ###############
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    ############# HOMEPAGE ##############
    path("homepage/", views.homepage, name="homepage"),
    ############# PROFILE ###############
    path("user/<username>/", views.dashboard, name="dashboard"),
    ############## FOOD API ##############
    path("api/find_food/", views.food_find, name="food_find"),
=======
  ############## LOG IN ###############
  path('', views.landing, name="landing"),
  path('index/', views.index, name="index"),
  path('login/', views.login_view, name="login"),
  path('signup/', views.signup_view, name="signup"),
  path('logout/', views.logout_view, name="logout"),
  ############# HOMEPAGE ##############
  path('homepage/', views.homepage, name="homepage"),
  ############# PROFILE ###############
  path('user/<username>/', views.dashboard, name='dashboard'),
>>>>>>> upstream/master
]
