
from django.contrib import admin
from django.urls import path, re_path

from app import views
urlpatterns = [
   
   path('',views.home,name='home'),
   path('sendEmail',views.sendEmail,name='sendEmail'),
   path('survey_status',views.survey_status,name='survey_status'),
   path('dashboard',views.dashboard,name='dashboard'),
   path('createAdmin',views.createAdmin,name='createAdmin'),
   path('logoutAdmin',views.logoutAdmin,name='logoutAdmin'),
   path('loginAdmin',views.loginAdmin,name='loginAdmin'),
   path('generateSurvey',views.generate_survey,name='generate_survey'),
   path('generateReport',views.generate_report,name='generate_report'),
   path('uploadCSV',views.uploadCSV,name='uploadCSV'),
   path('report',views.test,name='test')

]