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
