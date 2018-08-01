from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #   model = User
    #   fields = ['username', 'password', 'confirm_password']


# class CreateCircuitForm(forms.form):
#     name = models.CharField(max_length=50)
#     workouts = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='circuits')


# class CreateMealForm(forms.form):
#     label = models.CharField(max_length=100)
#     ingredients = models.TextField()
#     instructions = models.TextField()
#     portions = models.TextField()
#     macros = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
