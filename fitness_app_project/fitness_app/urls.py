from django.urls import path
from . import views

urlpatterns = [
  ############## LOG IN ###############
  path('', views.login_view, name="login"),
  path('logout/', views.logout_view, name="logout"),
  ############# HOMEPAGE ##############
  path('homepage/', views.homepage, name="homepage"),
  ############# PROFILE ###############
  path('user/<username>/', views.dashboard, name='dashboard'),
]
