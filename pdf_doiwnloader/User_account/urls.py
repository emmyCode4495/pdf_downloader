from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import SignUpForm
from . import views

urlpatterns =[
    #path('signup_successful/',views.home_page, name="home"),
    path('signup/',views.sign_up, name="signup"),
    #path('signup/done/',views.sign_up, name="sigup_done"),
    path('login/',views.log_in, name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('password_change/',
          auth_views.PasswordChangeView.as_view(), 
          name="password_change"),
    path('password_change/done/',
          auth_views.PasswordChangeDoneView.as_view(),
          name="password_change_done"),
    path('reset_password/',
          auth_views.PasswordResetView.as_view(),
          name="password_reset"),
    path('reset_password/done/',
          auth_views.PasswordResetDoneView.as_view(),
          name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(),
          name="password_reset_confirm"),
    path('reset_password/complete/',
          auth_views.PasswordResetCompleteView.as_view(),
          name="password_reset_complete")



]