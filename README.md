# airport-information-management-system
# Getting Started


* clone the project in your local computer
```
$ git clone https://github.com/kaul14/airport-information-management-system
```

## Prerequisites



```
- python3
- python3-pip
- virtualenvwrapper
- postgresql
- postgresql-contrib
- python-dev
- libpq-dev
- django
```



## Installing and Running the project

```
$ cd airport-information-management-system
```
```
$ pip install -r requirement.txt
```

```
$ python manage.py makemigrations
```
>if any prompt choose option 1
```
$ python manage.py migrate
```
> ignore some errors
```
$ python manage.py runserver
```
you will see something like This
```
Performing system checks...

System check identified no issues (0 silenced).
July 13, 2020 - 11:12:24
Django version 3.0, using settings 'Project_SLS.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Redirect at the link shown.

> use ctrl+c to stop the server and execute other command whenever needed.

## populating the data
Populate the data using admin panel

### creating superuser(admin)
```
$ python manage.py createsuperuser
```
> Fill the data asked in prompt


> run the server again
```
$ python manage.py runserver
```
> redirect to http://127.0.0.1:8000/admin.

> Login using the Email and Password you provided during creation of super user.


> populate some data of custom tags, Projects, softwares, activities.


> other data can be populated using the main app itself.
