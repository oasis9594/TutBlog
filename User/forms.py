#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
	password = forms.CharField(label="Password", max_length=30, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'}))

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, 
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'Email'}))
	username = forms.CharField(label="Username", max_length=30,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
	password1 = forms.CharField(label="Password", max_length=30, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1', 'placeholder': 'Password'}))
	password2 = forms.CharField(label="Password", max_length=30, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1', 'placeholder': 'Confirm Password'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', )