from django.urls import path
from . import views

urlpatterns=[
    path('user/register',views.User_SignUp),
    path('user/login',views.User_SignIn),
    path('user/<int:uid>/advisor',views.Get_Advisor),
    path('user/<int:uid>/advisor/<int:aid>',views.Book),
    path('user/<int:uid>/advisor/booking',views.GetBooking),
    ] 