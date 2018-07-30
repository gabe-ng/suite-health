from django.urls import path
from . import views

urlpatterns = [
    ############## LOG IN ###############
    path('', views.login_page, name="login_page"),

    ############# HOMEPAGE ##############

    ############# PROFILE ###############
]