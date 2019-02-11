# DjangoRestExample
Simple Django Rest example.

## Python

Suggested python>=3.6

## Install

```bash
$ python -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

## Run Server

```bash
(env) $ cd example
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py loaddata db.json
(env) $ python manage.py runserver
```

## Urls

**Home** http://127.0.0.1:8000/
**Admin** http://127.0.0.1:8000/admin/
**Students** http://127.0.0.1:8000/students/

