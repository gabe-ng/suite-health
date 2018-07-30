from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
      fields = ['username', 'password', 'password2']


# class CreateCircuitForm(forms.form):

# class CreateMealForm(forms.form):
