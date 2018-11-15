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


## Installation
**1. Install Python and virtualenv**
- **Python** (v.3.6.6 or newer)
    * The official download site: https://www.python.org/downloads/

- **Virtual Environment**
    ```bash
    $ pip install virtualenv
    ```
    For more information: https://virtualenv.pypa.io/en/latest/


**2. Install project and configuration**
1. Open **Terminal** and clone the project from [KhubKhao-Recommender](https://github.com/NokKbl/khubkhao-recommender.git).
    ```bash
    $ git clone https://github.com/NokKbl/khubkhao-recommender.git
    ```
2. Change your current working directory into `khubkhao-recommender` folder and create a new virtual environment.
    ```bash
    $ cd khubkhao-recommender
    $ virtualenv env
    ```
3. Activate the virtual environment.
    ```bash
    # For MacOS and Linux
    $ source ./env/bin/activate

    # For Windows
    $ .\env\Scripts\activate
    ```
4. Install all required software in `requirements.txt` file.
    ```bash
    (env)$ pip install -r requirements.txt
    ```
5. Run the commands below to make migrations, apply migrate, add seed data and run server.
    1. Make migrations.
        ```bash
        (env)$ python manage.py makemigrations
        ```
    2. Apply the migrations.
        ```bash
        (env)$ python manage.py migrate
        ```
    3. Add seed data to database.
        ```bash
        (env)$ python manage.py loaddata seed.json
        ```
    4. Run server at [127.0.0.1:8000](http://127.0.0.1:8000).
        ```bash
        (env)$ python manage.py runserver
        ```
    * If you want to login into admin site at [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin), you can do it by create superuser.
        ```bash
        (env)$ python manage.py createsuperuser
        ```
6. When done, exit virtualenv.
    ```bash
    (env)$ deactivate
    ```

## Team members
- [**Kornphon Noiprasert**](https://github.com/Driveiei) (ID: 6010545021)
- [**Kunyaruk Katebunlu**](https://github.com/NokKbl) (ID: 6010545692)
- [**Vichakorn Yotboonrueang**](https://github.com/Newaz2542) (ID: 6010545889)
