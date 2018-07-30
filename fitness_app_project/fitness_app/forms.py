from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> upstream/master
class SignupForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
<<<<<<< HEAD
=======

# class CreateCircuitForm(forms.form):

# class CreateMealForm(forms.form):
=======
>>>>>>> upstream/master
>>>>>>> upstream/master
