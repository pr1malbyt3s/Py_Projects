# Django Notes

Install Django using pip:
```pip install Django```
  
Install PostgreSQL:
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

Setup Database and Users:
- Create database and update permissions:
```
CREATE DATABASE djangodb;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE djangodb FROM PUBLIC;
```
- Create migration user role and assign permissions:
```
CREATE USER django_migrate WITH PASSWORD '<PASSWORD>' CREATEDB;
CREATE SCHEMA django_schema AUTHORIZATION django_migrate;
ALTER ROLE django_migrate SET SEARCH_PATH TO django_schema, public;
```
- Create app user role and assign permissions:
```
CREATE USER django_app WITH PASSWORD '<PASSWORD>';
ALTER ROLE django_app SET SEARCH_PATH TO django_schema;
```
- Create holistic Django read/write role and assign to app and migration users:
```
CREATE ROLE django_role;
GRANT CONNECT ON DATABASE djangodb TO django_role;
GRANT USAGE ON SCHEMA django_schema TO django_role;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA django_schema TO django_role;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA django_schema TO django_role;
GRANT django_role TO django_migrate;
GRANT django_role TO django_app;
```
- Alter migration user privileges:
```
ALTER DEFAULT PRIVILEGES FOR USER django_migrate GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO django_role;
ALTER DEFAULT PRIVILEGES FOR USER django_migrate GRANT USAGE, SELECT, UPDATE ON SEQUENCES TO django_role;
```
- Alter the Django settings.py DATABASES:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb',
        'USER': 'django_app',
        'PASSWORD': '<PASSWORD>',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    },
    'migration': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb',
        'USER': 'django_migrate',
        'PASSWORD': '<PASSWORD>',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

```
- Perform database migrations:
```python manage.py migrate --database=migration```
