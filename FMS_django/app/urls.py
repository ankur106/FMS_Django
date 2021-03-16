
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
   
   path('',views.home,name='home'),
   path('sendEmail',views.sendEmail,name='sendEmail'),
   path('success',views.success,name='success'),
   path('dashboard',views.dashboard,name='dashboard'),
   path('createAdmin',views.createAdmin,name='createAdmin'),
   path('logoutAdmin',views.logoutAdmin,name='logoutAdmin'),
   path('loginAdmin',views.loginAdmin,name='loginAdmin'),
   path('myfun',views.myfun,name='myfun')
]