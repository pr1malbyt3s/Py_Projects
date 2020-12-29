# Django Notes

## Install Django using pip:
```pip install Django```
  
## Install PostgreSQL:
- Download psycopg2:
```pip install psycopg2-binary```
- Create the file respository configuration:
```sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'```
- Import the repository signing key:
```wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -```
- Update the package lists:
```sudo apt-get update```
- Install latest PostgreSQL version:
```sudo apt-get -y install postgresql```
- Change PostgreSQL super user password:
```
sudo -u postgres psql postgres
\password postgres
```
## Setup Database and Users:
**Need to verify best security practices with users and app separation**
- Create database and update permissions:
```
CREATE DATABASE djangodb;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE djangodb FROM PUBLIC;
```
- Create app user role and assign permissions:
```
CREATE USER django_app WITH PASSWORD '<PASSWORD>';
GRANT CONNECT ON DATABASE djangodb TO django_app;
GRANT SELECT, UPDATE, INSERT, DELETE ON ALL TABLES IN SCHEMA public TO django_app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO django_app;
ALTER DEFAULT PRIVILEGES FOR USER django_app IN SCHEMA public GRANT SELECT, UPDATE, INSERT, DELETE ON TABLES TO django_app;
```
- Create migration user role and assign permissions:
```
CREATE USER django_migrate WITH PASSWORD '<PASSWORD>' CREATEDB;
ALTER DATABASE djangodb OWNER TO django_migrate;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO django_migrate;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO django_migrate;
```
- Create a password storage method:
-- Add the following to settings.py:
```
import json
from django.core.exceptions import ImproperlyConfigured

with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))
```
-- Add a secrets.json file in the base path:
```
{
	"APP_PASS": "<django_app_pass>",
	"MIGRATE_PASS": "<django_migrate_pass>",
	"SECRET_KEY": "<secret_key>"
}

```
- Alter the Django settings.py DATABASES:
**Need to adjust for separate settings file**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb',
        'USER': 'django_app',
        'PASSWORD': get_secret('APP_PASS'),
        'HOST': '127.0.0.1',
        'PORT': '5432'
    },
    'migration': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb',
        'USER': 'django_migrate',
        'PASSWORD': get_secret('MIGRATE_PASS'),
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

```
- Perform database migrations:
```python manage.py migrate --database=migration```
## Models:
Models are essentially the database layout and contain the essential fields and behaviors of stored data. An example using the polls app is below:
```
import datetime
from django.db import models
from django.utils import timezone

# Question model:
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice model:
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
```
## Admin site:
Pretty self-explanatory. Admin superusers are created by running ```python manage.py createsuperuser```. The admin.py file can be used to edit front end model content from an administrative perspective. An example can be seen below using the Question model in the polls app:
```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
## Views:
A view is a "type" of Web page in Django generally serving a specific function and having a specific template. Examples for the polls application include:
- Question 'index' page displaying the latest few question.
- Question 'detail' page displaying a question text and form to vote.
- Question 'results' page displaying particular question results.
- Vote action - handles voting for a particular choice in a particular question.
Each view is represented as a Python function or method. Views also need corresponding URL mappings. Below are examples of corresponding views.py and urls.py pages for the polls application:
```
# views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("At the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
```
# urls.py
from django.urls import path

from . import views

urlpatterns = [
    # Ex: /polls/
    path('', views.index, name='index'),
    # Ex: /polls/<#>/
    path('<int:question_id>/', views.detail, name='detail'),
    # Ex: /polls/<#>/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # Ex: /polls/<#>/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
**Need to add more about forms and generic views**
## Tests:
**Need to add a tests section**
## Static Files:
**Need to add a static files section**
