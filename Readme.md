+ Create a folder(anywhere you want)
+ open folder in vscode editor
+ open terminal 
+ from right side of the terminal select command prompt ( by default it selected with powershell)
+ make a vertual environment : `python -m venv venv`
+ Activate virtual environment : `venv\Scripts\activate`
+ Install Django : `pip install django`
+ Create a django project : `django-admin startproject app`
+ Run project 
    + Enter your project & run : `python manage.py runserver`
    + you can see your project run over : `http://127.0.0.1:8000/`
    + copy url and hit browser & enjoy your first Django run
+ Create a app inside project : `django-admin startapp app`