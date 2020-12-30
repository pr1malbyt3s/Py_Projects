# Django Notes

## Install Django using pip:
```sh
pip install Django
```
  
## Install PostgreSQL:
- Download psycopg2:
```sh
pip install psycopg2-binary
```
- Create the file respository configuration:
```sh
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```
- Import the repository signing key:
```sh
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```
- Update the package lists:
```sh
sudo apt-get update
```
- Install latest PostgreSQL version:
```sh
sudo apt-get -y install postgresql
```
- Change PostgreSQL super user password:
```sh
sudo -u postgres psql postgres
\password postgres
```
## Setup Database and Users:
- Create database and update permissions:
```sql
CREATE DATABASE djangodb;
```
**_Make sure you connect to the database before altering schema!_**
```sql
\c djangodb
```
```sql
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE djangodb FROM PUBLIC;
```
- Create migration user role and assign permissions:
```sql
CREATE USER django_migrate WITH PASSWORD '<PASSWORD>' CREATEDB;
CREATE SCHEMA <SCHEMA> AUTHORIZATION django_migrate;
ALTER ROLE django_migrate SET SEARCH_PATH TO <SCHEMA>, public;
```
- Create app user role and assign permissions:
```sql
CREATE USER django_app WITH PASSWORD '<PASSWORD>';
ALTER ROLE django_app SET SEARCH_PATH TO <SCHEMA>;
```
- Create a read/write role to cover shared permissions between the migration and app accounts:
```sql
CREATE ROLE django_rw;
GRANT CONNECT ON DATABASE djangodb TO django_rw;
GRANT USAGE ON SCHEMA <SCHEMA> TO django_rw;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA <SCHEMA> TO django_rw;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA <SCHEMA> TO django_rw;
GRANT django_rw TO django_migrate;
GRANT django_rw TO django_app;
```
- Alter the default privileges for the migration user:
```sql
ALTER DEFAULT PRIVILEGES FOR USER django_migrate GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO django_rw;
ALTER DEFAULT PRIVILEGES FOR USER django_migrate GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO django_rw;
```
-- In the event database issues arise, run the following sequence of commands to purge above actions:
```sql
DROP DATABASE djangodb;
DROP USER django_app;
DROP SCHEMA django;
ALTER DEFAULT PRIVILEGES FOR USER django_migrate REVOKE SELECT, INSERT, UPDATE, DELETE ON TABLES FROM django_rw;
ALTER DEFAULT PRIVILEGES FOR USER django_migrate REVOKE USAGE, SELECT, UPDATE ON SEQUENCES FROM django_rw;
DROP USER django_rw;
DROP USER django_migrate;
```
- Create a password storage method:
-- Add the following to settings.py:
```python
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
-- Add a secrets.json file in the base path with the following contents:
```json
{
	"APP_PASS": "<django_app_pass>",
	"MIGRATE_PASS": "<django_migrate_pass>",
	"SECRET_KEY": "<secret_key>"
}

```
- Alter the Django settings.py DATABASES:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb',
        'USER': 'django_app',
        'PASSWORD': get_secret('APP_PASS'),
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```
- Create an additional settings file (this example is titled migrate_settings.py) for migrations with the following contents:
```python
from .settings import *

DATABASES["default"]["USER"] = 'django_migrate'
DATABASES["default"]["PASSWORD"] = get_secret('MIGRATE_PASS')
```
- Perform database migrations:
```python manage.py migrate --settings=<MYSITE>.migration_settings```
## Models:
Models are essentially the database layout and contain the essential fields and behaviors of stored data. An example using the polls app is below:
```python
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
```python
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
```python
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
```python
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
