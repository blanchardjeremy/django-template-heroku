# django-template-heroku

This project is a template to get you started with a django project on the [Heroku](http://www.heroku.com/) hosting platform.

This template is a derivation of [django-template-auzigog](http://github.com/auzigog/django-template-auzigog) (which is good for non-Heroku projects).

(Note: This readme file gets removed and replaced with README.md.example for your actual project)

## Features
Pre-configured to work with:

  * Built for use with Django 1.5
  * Heroku!
  * [PostgreSQL](http://www.postgresql.org/) database
  * [Jinja2](http://jinja.pocoo.org/docs/) templates
  * [Jinja Bootstrap](http://github.com/auzigog/jinja-bootstrap/) for base templates and base styling
  * [django-debug-toolbar](http://github.com/django-debug-toolbar/django-debug-toolbar)
  * `.env` provided to separate machine-specific settings from universal settings
  * [Gunicorn](http://gunicorn.org/) WSGI server support when deployed to Heroku

## Setup
The following is the short version of the usage instructions. For the full version, check out [django-template-auzigog](http://github.com/auzigog/django-template-auzigog) and add the extra steps relating to Heroku.

    # Replace all instaces of PROJECTNAME with your project name
    pip install djenesis   # Install djenesis if you haven't already

    cd ~/Projects
    mkdir PROJECTNAME && cd PROJECTNAME
    djenesis PROJECTNAME --virtualenv=env git+https://github.com/auzigog/django-template-heroku.git
    mv PROJECTNAME code  # this is my preferred project folder structure
    cd code


## New Project Checklist
After starting a fresh project:

  1. Make a copy of `.env.example` called `.env` and edit it to contain your local settings including your database connection string
  1. Create your first app using SAMPLEAPP as a template
    1. Copy (don't rename) SAMPLE to a new directory for your new app. Example: `cp -R SAMPLEAPP blog`
    1. Add the new application to your `INSTALLED_APPS` in `settings.py`
    1. Specify new app name in `mainsite.urls`. Example: change `(r'', include('SAMPLEAPP.urls')),` to `(r'', include('blog.urls')),`
    1. In your new app, edit `urls.py` and change all instances of SAMPLEAPP to your app name.
    1. Add urls, views, and templates to your new app as necessary
  1. Delete `LICENSE` if it is not how you want to license your new project
  1. Delete this `README.md` file, rename `README.md.example` to `README.md`, replace with information for your current project
  1. Follow the *Usage* instructions in your new `README.md`


## Usage
Usage information is available in `README.md.example`


## License
This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)


## Credits
Created with love by [Jeremy Blanchard](http://blanchardjeremy.com)