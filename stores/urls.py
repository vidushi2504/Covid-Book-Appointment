from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('account/<int:id>', views.account, name='account'),
    path('editdetails', views.edit, name='editdetails'),
]