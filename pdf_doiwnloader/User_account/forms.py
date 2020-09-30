from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=500)
    first_name = forms.CharField(max_length=200, 
                                widget=forms.TextInput(attrs={'placeholder':'(e.g) Emmanuel'}))
    last_name = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={'placeholder':'(e.g) John'}))
    email = forms.EmailField(max_length=500,
                            widget=forms.TextInput(attrs={'placeholder':'(e.g) test@gmail.com'}),
                             help_text = "(Valid email address)")

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=500)
    password = forms.CharField(max_length=200,widget=forms.PasswordInput)