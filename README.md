# SMS Code Robot

================================================

## About Us

This is a sms code receive website.

## API Address

https://sms24.info/

~~https://smsreceivefree.com/~~

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

### 1、Get all countries

URL：

> /api/countries

Method：

> GET

### 2、Get all numbers

URL：

> /api/numbers

Method：

> GET

### 3、Get all numbers by country name

URL：

> /api/numbers/{country}/

Method：

> GET

REST Parameters：

| Name    | Value | Required | Remark                |
|---------|-------|----------|-----------------------|
| country | -     | Yes      | submit a country name |

### 4、Get all messages by number

URL：

> /api/messages/{number}/

Method：

> GET

REST Parameters：

| Name   | Value | Required | Remark          |
|--------|-------|----------|-----------------|
| number | -     | Yes      | submit a number |
