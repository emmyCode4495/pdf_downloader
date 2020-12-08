from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'login-field'}))
    first_name = forms.CharField(max_length=200, 
                                widget=forms.TextInput(attrs={'class':'login-field'}))
    last_name = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={'class':'login-field'}))
    email = forms.EmailField(max_length=500,
                            widget=forms.TextInput(attrs={'class':'login-field'}),
                             help_text = "(Valid email address)")

    class Meta:
        model = User  
        fields = ('username','first_name','last_name','email','password1','password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'login-field'}))
    password = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'class':'login-field'}))