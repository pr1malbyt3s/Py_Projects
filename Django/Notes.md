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

Setup Database User:
- Create user:
```
CREATE USER django;
```
