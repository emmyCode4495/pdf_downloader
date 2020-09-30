from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm, LoginForm

#Function Based view for home_page
def home_page(request):
    return HttpResponse("If you see this page smile ços(Registration Succesful)")

# Function based view for our sign up form
@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password = raw_password)
            login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request,'User_account\Register.html', context)

# function based view for log in
def log_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            login(request, user)
            return HttpResponse("Authenticated Successfully")
        else:
            return HttpResponse("Authentication failed")
    else:
        login_form = LoginForm()
    context = {'login_form':login_form}
    return render(request, "User_account\login.html", context)

