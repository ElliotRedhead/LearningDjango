# Learning Django

## Django To-Do Application

### Purpose / Scope

This project provides an example of a Django-based web app.  

## Instructional Notes

- Views and URLs are linked via the urls.py and views.py functions.  

- Ensure view functions are imported to urls.py alongside requirement in urlpatterns.

- Error: "TemplateDoesNotExist at /", ensure app name e.g."todo" is in the INSTALLED_APPS list of settings.py.

- To install sqlite3: download the .dll for the required OS, ensure environmental variables are configured for this.

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

5. Perform migration.  

   ``` console
   python3 manage.py migrate  
   ```

6. Access the in-built sqlite database.  

   ``` console
   sqlite3 db.sqlite3
   ```

7. View all tables in the listed database.  

   ``` sql
   select * from django_migrations;
   ```

8. View headers and show formatted columns.

   ``` sql
   .headers on
   .mode column
   ```

9. Quit sqlite3.

   ``` sql
   .quit
   ```

10. Create superuser.

    ``` console
    python3 manage.py createsuperuser
    ```

11. Apply models.

   ``` console
   python3 manage.py makemigrations
    ```

12. Running tests in tests.py.

   ``` console
   python3 manage.py tests
   ```

13. Run specific coverage test.

    ``` console
    coverage run --source=todo manage.py test
    ```

14. Generate coverage report.

    ``` console
    coverage html
    ```