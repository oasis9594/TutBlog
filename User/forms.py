#log/forms.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, Textarea
from User.models import Profile

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
	password = forms.CharField(label="Password", max_length=30, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'}))

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, 
		widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'Email'}))
	username = forms.CharField(label="Username", max_length=30,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
	password1 = forms.CharField(label="Password", max_length=30, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1', 'placeholder': 'Password'}))
	password2 = forms.CharField(label="Password", max_length=30, 
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1', 'placeholder': 'Confirm Password'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
	first_name = forms.CharField(label="First Name", max_length=30,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}))
	last_name = forms.CharField(label="Last Name", max_length=30,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}))
	email = forms.EmailField(max_length=254, 
		widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	mobile=forms.IntegerField(label="Mobile Number",
		widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'mobile'}))
	city = forms.CharField(label="City", max_length=30,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'city'}))
	country = forms.CharField(label="Country", max_length=30,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'country'}))
	bio = forms.CharField(label="About Me", max_length=500,
		widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'bio', 'rows': '2'}))
	class Meta:
		model = Profile
		fields = ('mobile', 'city', 'country', 'bio')
		