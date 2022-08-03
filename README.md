# SMS Code Robot

================================================

## About Us

This is a sms code receive website.

## API Address

https://sms24.info/

https://smsreceivefree.com/

## Files description

```python
manage.py  # Startup project file.
settings.py  # Project config file.
urls.py  # URL config file.
asgi.py  # Synchronous network request.
wsgi.py  # Asynchronous network request.
```

## Commands

```python
# Create a project by django-admin command.
django-admin startproject SMSCodeRobot
# Create an application to the project.
django-admin startapp APIModel
# Generate requirement files.
pip freeze > requirements.txt
# Run project.
python manage.py runserver 80
```

## Requirements

```python
django-4.0.6
beautifulsoup4-4.11.1
requests-2.28.1
```

## API

### 1、Country List

URL：

> http://127.0.0.1/api/countries

Method：

> GET

### 2、Number List

URL：

> http://127.0.0.1/api/numbers

Method：

> GET

Parameters：

| Name    | Value | Default | Required / Optional |
|---------|-------|---------|---------------------|
| country | -     | usa     | Optional            |

### 2、Number List

URL：

> http://127.0.0.1/api/info

Method：

> GET / POST

Parameters：

| Name   | Value | Default | Required / Optional |
|--------|-------|---------|---------------------|
| number | -     | -       | Required            |
| page   | -     | 1       | Optional            |

