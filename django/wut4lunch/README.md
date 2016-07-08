# wut4lunch sample app with Django

##Steps
1. `$ virtualenv .` (we'll use Python 2.7.11)
2. `$ source bin/activate`
3. `$ pip install -r requirements.txt`
4. `django-admin startproject wut4lunch .`
4. `python manage.py migrate`

### Run the server:
`$ python manage.py runserver`

### Make migrations
`$ python manage.py makemigrations wut4lunch`

### Run migrations:
`$ python manage.py migrate`
