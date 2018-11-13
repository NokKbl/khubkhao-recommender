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
**Khub-Khao Recommender** is a web application that gives food recommendations based on criteria specified by the user. The target group is users who can’t decide what to eat. The main features include:
1. Receive and analyze criteria specified by the user
2. Display dish types based on the criteria
3. Display dish ratings from our servers
4. Allow users to rate dishes


## Documents
- **Iteration plan**: [Iteration plan and details](https://github.com/NokKbl/khubkhao-recommender/wiki/Iteration-plan-and-details)
- **Task board**: [Task board on Waffle](https://waffle.io/NokKbl/khubkhao-recommender)
- **Issue tracking**: [GitHub issue tracker](https://github.com/NokKbl/khubkhao-recommender/issues)
- **Others**: [Our GitHub Wiki](https://github.com/NokKbl/khubkhao-recommender/wiki)


## Install and Run
**Required software:**
- **Python** (v.3.6.6)
    * The official download site: https://www.python.org/downloads/

- **Virtual Environment**
    ```bash
    $ pip install virtualenv
    ```
    For more information: https://virtualenv.pypa.io/en/latest/


**To install and run locally**
1. Open **Terminal** and clone the project from [KhubKhao-Recommender](https://github.com/NokKbl/khubkhao-recommender.git).
    ```bash
    $ git clone https://github.com/NokKbl/khubkhao-recommender.git
    ```
2. Change your current working directory into `khubkhao-recommender` folder and create a new virtual environment.
    ```bash
    $ cd khubkhao-recommender
    $ virtualenv <your_environment_name>
    ```
3. Activate the virtual environment.
    ```bash
    # For MacOS and Linux
    $ source ./<your_environment_name>/bin/activate

    # For Windows
    $ source ./<your_environment_name>/Scripts/activate
    ```
4. Install all required software in `requirements.txt` file.
    ```bash
    $ pip install -r requirements.txt
    ```
5. Run the commands below to make migrations, apply migrate, add seed data and run server.
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
