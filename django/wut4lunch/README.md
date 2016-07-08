# wut4lunch sample app with Django

##Steps
1. `$ virtualenv .` (we'll use Python 2.7.11)
2. `$ source bin/activate`
3. `$ pip install -r requirements.txt`
4. `django-admin startproject wut4lunch .`
4. `python manage.py migrate`

### Run the server:
`$ python manage.py runserver`

## Where can I see this app running?
Go to: https://wut4lunch-django.herokuapp.com/ (staging env)

### Make migrations
`$ python manage.py makemigrations wut4lunch`

### Run migrations:
`$ python manage.py migrate`

### Deploy to heroku
1. `cd directory`
2. `git init`
3. `heroku git:remote -a [repo-name]`
4. `git add .`
5. `git commit -m "I am THE code"`
6. `git push heroku master`
7. `heroku run python manage.py migrate`
9. `heroku ps:scale worker=1`
9. Check `heroku ps` to see that your worker comes up, and `heroku logs` to see your worker doing its work.
10. `heroku open`

## References
* https://devcenter.heroku.com/articles/deploying-python
* https://devcenter.heroku.com/articles/deploying-python#django-applications-on-heroku
* http://stackoverflow.com/questions/32790009/improperlyconfigured-staticfiles




