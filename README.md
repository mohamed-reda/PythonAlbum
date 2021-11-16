command lines to activate the venv:

cd venv\Scripts activate cd.. cd..

install django:
pip install django

start django project called core:

django-admin startproject core
(I should write "django-admin startproject core ." command)

start the application:

py manage.py runserver

py core\manage.py startapp blog

restart the server py manage.py runserver

I needed to install:
python -m pip install Pillow

to run this migrations:
py manage.py makemigrations

py manage.py migrate

16:38
