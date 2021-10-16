from django.urls import path
from user import views

urlpatterns=[
    path('accounts/signup',views.SignUpView.as_view(),name='signup'),
    path('accounts/signin',views.SignInViews.as_view(),name='login'),
    path('accounts/home',views.Home.as_view(),name='home'),
    path('accounts/signout',views.signout,name='logout'),
    path('accounts/order',views.CreateOrderViews.as_view(),name='makeorder'),
    path('accounts/cart',views.Cart.as_view(),name='cart'),
    path('cart/order/remove/<int:id>',views.remove,name='remove')

]