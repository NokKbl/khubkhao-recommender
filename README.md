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
- **Iteration plan**: [Iteration plan and details](https://github.com/NokKbl/khubkhao-recommender/wiki/Iteration-plan-and-details)
- **Task board**: [Task board on Waffle](https://waffle.io/NokKbl/khubkhao-recommender)
- **Issue tracking**: [GitHub issue tracker](https://github.com/NokKbl/khubkhao-recommender/issues)
- **Others**: [Our GitHub Wiki](https://github.com/NokKbl/khubkhao-recommender/wiki)


## Install and Run
**Required software:**
- **Python** (v.3.6.6)

    * The official download site: https://www.python.org/downloads/

- **Django** (v.2.1.2)
    ```bash
    $ pip install django
    ```
    For more information: https://www.djangoproject.com/

- **python-decouple**
    ```bash
    $ pip install python-decouple
    ```
    For more information: https://pypi.org/project/python-decouple/

- **Django-Heroku** package
    ```bash
    $ pip install django-heroku
    ```
    For more information: https://pypi.org/project/django-heroku/


**To install and run locally**
1. Clone project from [KhubKhao-Recommender](https://github.com/NokKbl/khubkhao-recommender.git).
2. Install all required software in `requirements.txt` file.
    ```bash
    $ pip install -r requirements.txt
    ```
3. Open Terminal and run commands below.
    1. Make migrations.
        ```bash
        $ python manage.py makemigrations
        ```
    2. Apply the migrations.
        ```bash
        $ python manage.py migrate
        ```
    3. Add seed data to database.
        ```bash
        $ python manage.py loaddata seed.json
        ```
    4. Run server at [127.0.0.1:8000](http://q1127.0.0.1:8000).
        ```bash
        $ python manage.py runserver
        ```
    * If you want to login into admin site at [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), you can do it by create superuser.
        ```bash
        $ python manage.py createsuperuser
        ```


## Team members
- [**Kornphon Noiprasert**](https://github.com/Driveiei) (ID: 6010545021)
- [**Kunyaruk Katebunlu**](https://github.com/NokKbl) (ID: 6010545692)
- [**Vichakorn Yotboonrueang**](https://github.com/Newaz2542) (ID: 6010545889)
