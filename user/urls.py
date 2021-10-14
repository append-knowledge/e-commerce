from django.urls import path
from user import views

urlpatterns=[
    path('accounts/signup',views.SignUpView.as_view(),name='signup'),
    path('accounts/signin',views.SignInViews.as_view(),name='login'),
    path('accounts/home',views.Home.as_view(),name='home')

]