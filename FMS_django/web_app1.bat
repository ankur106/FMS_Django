@echo off

title FMS_Django.exe
f:
cd F:\college\sem 6\3CP08\FMS_Django\FMS_django  
web_app1\Scripts\activate & python manage.py runserver 0.0.0.0:8000 | start http://localhost:8000/ && PAUSE
 


