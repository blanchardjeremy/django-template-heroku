# django-template-heroku

This project is a template to get you started with a django project on the [Heroku](http://www.heroku.com/) hosting platform.

This template is a derivation of [django-template-auzigog](http://github.com/auzigog/django-template-auzigog) (which is good for non-Heroku projects).

## Setup & Usage
The following is the short version of the usage instructions. For the full version, check out [django-template-auzigog](http://github.com/auzigog/django-template-auzigog) and add the extra steps relating to Heroku.

    cd ~/Projects
    djenesis PROJECTNAME/code --virtualenv=PROJECTENV/env git+https://github.com/auzigog/django-template-heroku.git
    cd PROJECTNAME/code
    source .env_local
    source ../env/bin/activate
    git init
    git add -A
    git commit -m 'Big bang! Initial commit of PROJECTNAME'

Further setup and usage information is available below in the template setup file.

## License
This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)

## Project README
When starting a project, delete everything in this readme above this line (see below) and you will have a template for your project's README.


DELETE EVERYTHING ABOVE THIS LINE WHEN MAKING A NEW PROJECT -- The text below will server as your actual project README

***********************************************************************************************************************

# {{ project_name }}

## Dependencies

## Local Settings
Heroku's system requires that local (per-environment) settings be started as operating system environment variables.

For your development environment, specify settings in the `.env_local` file and then retreive them in settings.py like so:
```python
MY_SETTING = os.environ.get('MY_SETTING', 'default value here if setting isnt specified at the OS level')
```

## Usage
When you begin working on this project, do the following:

    cd ~/Projects/thisproject/code
    source .env_local               # Load local settings
    source ../env/bin/activate      # Load the virutalenv for this project
    ./manage.py runserver           # Launch your server. Visit http://localhost:8000/


## Author
Created by [Your Name](http://example.com)