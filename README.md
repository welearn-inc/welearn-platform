# WeLearn 
[![WeLearn Logo](http://welearn.com.co/assets/images/WeLearn_Horizontal.svg)
](http://welearn.com.co/)

We imagine a new system for learning. One that is global in nature, accessible to all, and time and place independent.
This system should allow students to have greater control over their learning experience, and reward instructors who provide the most innovative, highest quality instruction.

# Installation

### Linux
```
$ git clone https://github.com/welearn-inc/welearnapp.git
$ cd welearnapp/backend
$ virtualenv .
$ source ./bin/activate
$ pip install -r requirements
$ cd src
$ python manage.py migrate
$ python manage.py runserver
```

### Windows
```
$ git clone https://github.com/welearn-inc/welearnapp.git
$ cd welearnapp\backend
$ virtualenv .
$ Scripts\activate
$ python -m pip install -r requirements.txt
$ cd src
$ python manage.py migrate
$ python manage.py runserver
```

# Tools
* Python 3.x.x
* Django 1.11.8
* Django Rest Framework 3.7.7
* SQLite