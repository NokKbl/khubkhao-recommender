# KHUB-KHAO RECOMMENDER

![bg](khubkhaoapp/static/khubkhaoapp/images/bg.png)

- Status of last [Travis CI build](https://travis-ci.org/NokKbl/khubkhao-recommender): [![Build Status](https://travis-ci.org/NokKbl/khubkhao-recommender.svg?branch=master)](https://travis-ci.org/NokKbl/khubkhao-recommender)

- Status of all columns [Waffle Badge](https://waffle.io/NokKbl/khubkhao-recommender): [![Waffle.io - Columns and their card count](https://badge.waffle.io/NokKbl/khubkhao-recommender.svg?columns=all)](https://waffle.io/NokKbl/khubkhao-recommender)

**Table of contents**
- [Description](#description)
- [Team members](#team-members)
- [Documents](#documents)
- [Installation Instructions](#installation-instructions)
- [How to Run](#how-to-run)


## Description
**Khub-Khao Recommender** is a web application that gives food recommendations based on criteria specified by the user. The target group is users who can’t decide what to eat. The main features include:
1. Receive and analyze criteria specified by the user
2. Display dish types based on the criteria
3. Display dish ratings from our servers
4. Allow users to rate dishes


## Team members
Team members | GitHub | Role(s)
-------------|--------|----------
Vichakorn Yotboonrueang | [**Newaz2542**](https://github.com/Newaz2542) | Team Leader, Developer
Kunyaruk Katebunlu | [**NokKbl**](https://github.com/NokKbl) | Developer
Kornphon Noiprasert | [**Driveiei**](https://github.com/Driveiei) | Developer


## Documents
- **Iteration plan**: [Iteration plan and details](https://github.com/NokKbl/khubkhao-recommender/wiki/Iteration-plan-and-details)
- **Task board**: [Task board on Waffle](https://waffle.io/NokKbl/khubkhao-recommender)
- **Issue tracking**: [GitHub issue tracker](https://github.com/NokKbl/khubkhao-recommender/issues)
- **Others**: [Our GitHub Wiki](https://github.com/NokKbl/khubkhao-recommender/wiki)


## Installation Instructions
**1. Install Python and virtualenv.**
- **Python** (v.3.6.6 or newer)
    * The official download site: https://www.python.org/downloads/

- **Virtual Environment**
    ```bash
    $ pip install virtualenv
    ```
    For more information: https://virtualenv.pypa.io/en/latest/

**2. Install project and configuration.**
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
5. Change a file name `.env.example` into `.env`.


## How to run
**Run the following commands to make migrations, apply migrate, add seed data and run server.**
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
4. Run server at [localhost:8000](http://localhost:8000).
    ```bash
    (env)$ python manage.py runserver
    ```
**Social account for Tester** (include Facebook, Twitter and Google Plus)
- **Email:** dxvtxxtxr@gmail.com
- **Password:** XXXXXXXXXXXXXX

**If you want to login into admin site at [localhost:8000/admin](http://localhost:8000/admin), you can do it by create superuser.**
```bash
(env)$ python manage.py createsuperuser
```

**When done, exit virtualenv.**
```bash
(env)$ deactivate
```
