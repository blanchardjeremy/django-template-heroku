# django-template-heroku

This project is a template to get you started with a django project on the [Heroku](http://www.heroku.com/) hosting platform.

This template is a derivation of [django-template-auzigog](http://github.com/auzigog/django-template-auzigog) (which is good for non-Heroku projects).

## Features
Pre-configured to work with:

  * Heroku!
  * [PostgreSQL](http://www.postgresql.org/)
  * [Jinja2](http://jinja.pocoo.org/docs/) templates
  * [django-debug-toolbar](http://github.com/django-debug-toolbar/django-debug-toolbar)
  * `.env_local` provided to separate machine-specific settings from universal settings

## Setup
The following is the short version of the usage instructions. For the full version, check out [django-template-auzigog](http://github.com/auzigog/django-template-auzigog) and add the extra steps relating to Heroku.

    # Replace all instaces of PROJECTNAME with your project name
    pip install djenesis   # Install djenesis if you haven't already

    cd ~/Projects
    djenesis PROJECTNAME/code --virtualenv=PROJECTENV/env git+https://github.com/auzigog/django-template-heroku.git
    cd PROJECTNAME/code


## New Project Checklist
After starting a fresh project:

  1. Rename `.env.example` to `.env` and edit it to contain your local settings including your database connection string
  1. Delete this `README.md` file, rename `README.md.example` to `README.md`, replace with information for your current project
  1. Create your first app using SAMPLEAPP as a template. These steps use
    1. Copy (don't rename) SAMPLE to a new directory for your new app. Example: `cp -R SAMPLEAPP blog`
    1. Specify new app name in `mainsite.urls`. Example: change `(r'', include('SAMPLEAPP.urls')),` to `(r'', include('blog.urls')),`
    1. Add urls, views, and templates to your new app as necessary


## Usage
Usage information is available in `README.md.example`


## License
This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)


## Credits
Created with love by [Jeremy Blanchard](http://blanchardjeremy.com)