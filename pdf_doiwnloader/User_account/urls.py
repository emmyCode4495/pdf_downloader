from django.urls import path

from .forms import SignUpForm
from . import views

urlpatterns =[
    path('signup_successful/',views.home_page, name="home"),
    path('signup/',views.sign_up, name="signup")
]