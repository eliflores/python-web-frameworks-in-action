# How to re-create the project?

* `cd django`
* `python3 -m venv myvenv`
* `source myvenv/bin/activate`
* `pip install django~=1.9.0`
* `django-admin startproject hello_django`
* `cd hello_django`
* `python manage.py runserver`
* Go to http://127.0.0.1:8000/
* `Ctrl + C` to stop the server`
* `cd hello_django`
* `python manage.py startapp howdy`
* `python manage.py runserver`
* Go to http://127.0.0.1:8000/howdy

## References

* https://docs.djangoproject.com/en/1.9/intro/tutorial01/
* http://docs.python-guide.org/en/latest/dev/virtualenvs/
* https://www.airpair.com/python/posts/django-flask-pyramid