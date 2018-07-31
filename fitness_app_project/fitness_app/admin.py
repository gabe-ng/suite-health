from django.contrib import admin
from .models import User, Profile, Custom_Meal, Custom_Circuit, Food

admin.site.register(Profile)
admin.site.register(Custom_Meal)
admin.site.register(Custom_Circuit)
admin.site.register(Food)
