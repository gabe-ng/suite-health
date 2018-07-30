from django.urls import path
from . import views

urlpatterns = [
  ############## LOG IN ###############
  path('', views.index, name="login"),
  ############# HOMEPAGE ##############
  path('/homepage', views.homepage, name="homepage"),
  ############# PROFILE ###############
  path('user/<username>/', views.profile, name='profile'),
]