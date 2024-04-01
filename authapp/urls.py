from django.urls import path, include
from . import views
from django.contrib import admin

app_name = "authapp"

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.LoginViewUser.as_view(), name='login'),
    path('signupseller/',views.RegisterViewSeller.as_view(), name='signupseller'),
    path('signup/',views.RegisterView.as_view(), name="signup"),
]