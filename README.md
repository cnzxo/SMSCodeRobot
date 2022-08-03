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
```

## API

### Interface 1

URL：

> http://127.0.0.1/api/numbers

Method：

> GET / POST

Parameters：

| Name    | Value      | Default | Required / Optional |
|---------|------------|---------|---------------------|
| country | usa、canada | usa     | Optional            |

