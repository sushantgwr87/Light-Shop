<p align="center">
    <a href="https://www.heroku.com/"><img src="https://img.shields.io/badge/-Heroku Hosted-8C6DB1?style=flat&logo=heroku&logoColor=FFFFFF" alt="Heroku" height="30"></a>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/-Django-1f6E16?style=flat&logo=django&logoColor=000000" alt="django" height="30">
    &nbsp; &nbsp; 
    <img src="https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white" alt="HTML5" height="28">
    &nbsp; &nbsp; 
    <img src="https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3" alt="CSS" height="28">
    &nbsp; &nbsp; 
    <img src="https://img.shields.io/badge/-python-E9FA2f?style=flat&logo=python&logoColor=000000" alt="python" height="28">
    &nbsp; &nbsp; 
    <img src="https://img.shields.io/badge/-JavaScript-000000?style=flat&logo=javascript" alt="Javascript" height="30">
</p>
&nbsp; 

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

    SECRET_KEY = API key

In settings.py this key is used as:

    SECRET_KEY = config('The variable name in .env inside quotes')

If you store API key as string in .env then remove quotations inside config.
- In .env file
        
        SECRET_KEY = 'API key'
    
- In settings.py

        SECRET_KEY = config(SECRET_KEY)
