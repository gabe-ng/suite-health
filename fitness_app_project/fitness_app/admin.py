from django.contrib import admin
from .models import User, Custom_Meal, Custom_Circuit

admin.site.register(User)
admin.site.register(Custom_Meal)
admin.site.register(Custom_Circuit)
