

poetry init
poetry add flask flask-smorest
poetry add --dev pytest pytest-flask
poetry add --dev requests

poetry shell
FLASK_APP=app:server flask run --reload
poetry run pytest -v

http://127.0.0.1:5000/docs

Sometimes the env is broken.
poetry env remove python
poetry env use python3

# Python - Flask framework

This guide explains how to build a robust API with Flask Python on a Linux system.

About Flask: https://www.youtube.com/watch?v=mt-0F_5KvQw

### Stack
<b><u>
Python

Flask</u></b>

### Start Application

```
poetry shell

FLASK_APP=app:server flask run --reload
```
---

### Visit

http://127.0.0.1:5000/docs



### Run Tests
```
poetry run pytest -v
```

### Installation
```
poetry init

poetry add flask flask-smorest

poetry add --dev pytest pytest-flask

poetry add --dev requests
```


### Sometimes the env is broken.
```
poetry env remove python
```

```
poetry env use python3
```