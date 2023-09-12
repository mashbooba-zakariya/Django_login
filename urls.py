from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('home/',views.home,name='home'),
    path('signin/',views.signin_page,name='signin'),
    path('logout/',views.logout_page,name='logout')
]