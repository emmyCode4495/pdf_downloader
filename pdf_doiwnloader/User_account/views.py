from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

from .forms import SignUpForm

#Function Based view for home_page
def home_page(request):
    return HttpResponse("If you see this page smile ços(Registration Succesful)")

# Function based view for our sign up form
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

