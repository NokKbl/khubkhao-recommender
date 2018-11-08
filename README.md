# KHUB-KHAO RECOMMENDER

![bg](khubkhaoapp/static/khubkhaoapp/images/bg.png)

- Status of last [Travis CI build](https://travis-ci.org/NokKbl/khubkhao-recommender): [![Build Status](https://travis-ci.org/NokKbl/khubkhao-recommender.svg?branch=master)](https://travis-ci.org/NokKbl/khubkhao-recommender)

- Status of all columns [Waffle Badge](https://waffle.io/NokKbl/khubkhao-recommender): [![Waffle.io - Columns and their card count](https://badge.waffle.io/NokKbl/khubkhao-recommender.svg?columns=all)](https://waffle.io/NokKbl/khubkhao-recommender)

**Table of contents**
- [Description](#description)
- [Documents](#documents)
- [Install and Run](#install-and-run)
- [Team members](#team-members)

## Description

**Khub-Khao Recommender** is a web application which will be a food recommender that based on criteria specified by the user. The intended users are everyone that can’t decided what to eat. The main features are get criteria specified by the user then analyze and show foods in the category based on the requirement, show rating of foods from our server and users able to rate foods if they want.


## Documents
- Iteration plan: [Iteration plan and details](https://github.com/NokKbl/khubkhao-recommender/wiki/Iteration-plan-and-details)
- Task board: [Task board on Waffle](https://waffle.io/NokKbl/khubkhao-recommender)
- Issue tracking: [GitHub issue tracker](https://github.com/NokKbl/khubkhao-recommender/issues)
- Others: [Our GitHub Wiki](https://github.com/NokKbl/khubkhao-recommender/wiki)


## Install and Run
**Required software:**
- **Python** (v.3.6.6)

    * The official download site: https://www.python.org/downloads/

- **Django** (v.2.1.2)
    ```console
    $ pip install django
    ```
For more information: https://www.djangoproject.com/


**To install and run locally**
1. Clone project from [KhubKhao-Recommender](https://github.com/NokKbl/khubkhao-recommender.git).
2. Edit `settings.py` file.
    1. Remove/comment these lines in the file.
        ```python
        import django_heroku
        from decouple import config
        ```
    2. Add `127.0.0.1` into `ALLOWED_HOSTS`.
        ```
        ALLOWED_HOSTS = ['.herokuapp.com', '.localhost','127.0.0.1']
        ```
    3. Scroll down to `DATABASES` and change from using PostgreSQL as a database
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'khubkhao_db',
                'USER': config('KKR_USER_DB'),
                'PASSWORD': config('KKR_PWD_DB'),
                'HOST': config('KKR_HOST_DB'),
                'PORT': '5432',
            }
        }
        ```
        into SQLite.
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
        }
        ```
    4. Scroll to the bottom of the file then remove.
        ```python
        django_heroku.settings(locals())
        ```
        and put the code below instead.
        ```python
        STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
        ```
3. Open Terminal and run commands below.
    1. Make migrations.
        ```console
        $ python manage.py makemigrations
        ```
    2. Apply the migrations.
        ```console
        $ python manage.py migrate
        ```
    3. Run server at [127.0.0.1:8000](127.0.0.1:8000).
        ```console
        $ python manage.py runserver
        ```
    * If you want to login into admin site at [127.0.0.1:8000/admin](127.0.0.1:8000/admin), you can do it by create superuser.
        ```console
        $ python manage.py createsuperuser
        ```


## Team members
- [**Kornphon Noiprasert**](https://github.com/Driveiei) (ID: 6010545021)
- [**Kunyaruk Katebunlu**](https://github.com/NokKbl) (ID: 6010545692)
- [**Vichakorn Yotboonrueang**](https://github.com/Newaz2542) (ID: 6010545889)
