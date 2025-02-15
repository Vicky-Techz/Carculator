from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form email'}))
  first_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'form firstname'}))
  last_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'form lastname'}))
  username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'form username', 'placeholder':'User name'}))
  password1 = forms.CharField(label="Password", max_length=255, required=True, widget=forms.PasswordInput(attrs={'class':'form password', 'placeholder':'Password'}))
  password2 = forms.CharField(label="Password Confirmation", max_length=255, required=True, widget=forms.PasswordInput(attrs={'class':'form password', 'placeholder':'Confirm Password'}))
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email', 'username']

# class LoginForm(AuthenticationForm):
#   username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class':'form username', 'placeholder':'Username'}))
#   password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'class':'form password', 'placeholder':'Password'}))