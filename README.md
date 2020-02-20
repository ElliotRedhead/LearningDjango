# Learning Django

## Django To-Do Application

### Purpose / Scope

This project provides an example of a Django-based web app.  

## Instructional Notes

- Views and URLs are linked via the urls.py and views.py functions.  

- Ensure view functions are imported to urls.py alongside requirement in urlpatterns.

- Error: "TemplateDoesNotExist at /", ensure app name e.g."todo" is in the INSTALLED_APPS list of settings.py.

### Commands

1. Install a specific version of Django that is compatible with the CI course instructional content:  

``` console
pip3 install django==1.11.24
```

2. Create a Django project "a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings."  

``` console
django-admin startproject django_todo .
```

3. Run the Django project server.  

``` console
python3 manage.py runserver
py manage.py runserver
```

4. Create an app called "todo".  

``` console
django-admin startapp todo
```

5. Access the in-built sqlite database.  

``` console
sqlite3 db.sqlite3
```

6. View all tables in the listed database.  

``` sqlite3
select * from django_migrations;
```

7. View headers and show formatted columns.

``` sqlite3
.headers on
.mode column
```

8. Quit sqlite3.

``` sqlite3
.quit
```
