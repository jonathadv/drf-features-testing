# drf-feautures-testintg

Repository to test the Django Rest Framework features

# Quickstart
[Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)

Install dependencies
```bash
$ pipenv install django djangorestframework markdown django-filter pygments
$ pipenv shell
````

Start the project
```bash
$ django-admin startproject tutorial .
$ cd tutorial
$ django-admin startapp quickstart
$ cd ..
$ python manage.py migrate
$ python manage.py createsuperuser --email admin@example.com --username admin
$ python manage.py runserver
```