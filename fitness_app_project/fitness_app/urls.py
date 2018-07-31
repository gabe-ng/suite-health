from django.urls import path
from . import views

urlpatterns = [
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
  ############# FOOD API #################
  path('api/food/find', views.find_food, name='find_food'),
  ############# WORKOUT API #################
]
