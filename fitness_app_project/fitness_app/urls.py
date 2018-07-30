from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    ############## LOG IN ###############
    path("", views.index, name="login"),
    ############# HOMEPAGE ##############
    path("homepage/", views.homepage, name="homepage"),
    ############# PROFILE ###############
    path("user/<username>/", views.profile, name="profile"),
    ############# SPECIFIC FOOD ###############
    path("food/", views.food_view, name="food_view"),
=======
  ############## LOG IN ###############
  path('', views.index, name="index"),
  path('login/', views.login_view, name="login"),
  path('signup/', views.signup_view, name="signup"),
  path('logout/', views.logout_view, name="logout"),
  ############# HOMEPAGE ##############
  path('homepage/', views.homepage, name="homepage"),
  ############# PROFILE ###############
  path('user/<username>/', views.dashboard, name='dashboard'),
>>>>>>> upstream/master
]
