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
+ Configure project `settings.py` to configure our new `app`
    + Go to `settings.py`. Then inside `INSTALLED_APPS = []` list, add `'app',` which is your created appName
    + Create a `templates` foder inside project directory. Where `app,manage.py,templaes` ar in same lavel
    + Go to `settings.py`. Then nnside `TEMPLATES = []` list, add `'DIRS': ['templates']`
    + Inside templates folder create a `index.html` file & just write something, like Hello world in html file
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Django App</title>
        </head>
        <body>
            <h1>Hello world</h1>
        </body>
        </html>
        ```
    + Now to connect app `urls.py`, with main project `urls.py`, create `urls.py` inside `app`
        ```python
        from django.urls import path

        urlpatterns = [
            
        ]
        ```
    + Go to app `views.py` & create a function `index`
        ```python
        def index(request):
            return render(request,'index.html')
        ```
    + Go to again app `urls.py` & include `views index function` for specific url
        ```python
        from app import views
        from django.urls import path,include

        urlpatterns = [
            path('',include(views.index,name="index"))
        ]
        ```
    + Go to project `urls.py` & include `app urls.py` file
        ```python
        from django.contrib import admin
        from django.urls import path,include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('',include('app.urls'))
        ]
        ```
    + Close & rerun server again. Your index.html file should see in the browser successfully