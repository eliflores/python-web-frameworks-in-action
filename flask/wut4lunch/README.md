#Steps
1. `$ python3 -m venv venv`
2. `$ source venv/bin/activate`
3. `$ pip install -r requirements.txt`
4. `$ echo "source 'which activate.sh'" >> ~/.bash_profile`
5. `$ source ~/.bash_profile`


## Init database
1. You need to have Postgres installed and running
2. Create a database called `wut4lunch_flask_dev` (local development database)
1. `$ python manage.py db init`
2. `$ python manage.py db migrate`
3. `$ python manage.py db upgrade`

### Reference 
https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/

## Where can I see this app running?
Go to: https://wut4lunch-flask.herokuapp.com/
[This is running with StagingConfig]

# References

* https://www.airpair.com/python/posts/django-flask-pyramid#6-frameworks-in-action
* http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#quickstart
* http://flask.pocoo.org/docs/0.11/patterns/packages/
* https://community.nitrous.io/tutorials/deploying-a-flask-application-to-heroku
* http://stackoverflow.com/questions/35145728/gunicorn-connection-in-use-for-python-flask
* https://devcenter.heroku.com/articles/deploying-python
* https://realpython.com/blog/python/flask-by-example-part-1-project-setup/
* https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
* https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app

