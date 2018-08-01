from django.urls import path
from . import views

urlpatterns = [
    ############## LOG IN/LOG OUT###############
    path('', views.landing, name="landing"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    ############# HOMEPAGE ##############
    path('homepage/', views.homepage, name="homepage"),
    path('homepage/custommeals/', views.custom_meals, name="custommeals"),
    path('homepage/customcircuits/', views.custom_circuits, name="customcircuit"),
    ############# PROFILE ###############
    path('user/<username>/', views.dashboard, name='dashboard'),
    ############# FOOD API #################
    path('api/food/find/<slug:food>', views.find_food, name='find_food'),
    ############# WORKOUT API #################
    path('api/workout/find/<slug:muscle>', views.find_workout, name='find_workout'),
    path('api/workout/<int:pk>/save', views.save_workout, name='save_workout'),
]
