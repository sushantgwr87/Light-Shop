# Light Shop

A Light shop ecommerce website with SQL database implemented using Django framework.

## Details

### Folder and App directory
The lightshop is project name and home is backened-app name in development process.

### HTML Template
HTML components/pages are made dynamic using django-html to use python variables and loops in html.  base.html file contains all header files and is the root template which is rendered i.e all other html files are imported in it.

### Routing
All routes are in url.py(both in home directory and in lightshop directory), each template page is routed with specific functions in views.py to show data as per needed.

### Database
SQLite is used for database. Backened-database can be accessed only by admin panel inbuild in django framework. modal.py shows declaration and defining of database's variables as well as their values.

### Procfile
For Heroku hosting via gunicorn package.

### Styling
Bootstrap version 5 is used for ease of designing.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY = API key`

In settings.py this key is used :

`SECRET_KEY = config('The variable name in .env')`

In my case, variable name is SECRET_KEY name itself :

`SECRET_KEY = config('SECRET_KEY')`

### Note
If you store API key as string in .env then remove quotations inside config.

In .env file

`SECRET_KEY = 'API key'`

In settings.py

`SECRET_KEY = config(SECRET_KEY)`
