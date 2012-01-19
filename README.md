# django-template-heroku

This project is a template to get you started with a django project on the [Heroku](http://www.heroku.com/) hosting platform.

This template is a derivation of [django-template-auzigog](http://github.com/auzigog/django-template-auzigog) (which is good for non-Heroku projects).

## Setup & Usage
The following is the short version of the usage instructions. For the full version, check out [django-template-auzigog](http://github.com/auzigog/django-template-auzigog) and add the extra steps relating to Heroku.

    cd ~/Projects
    djenesis PROJECTNAME/code --virtualenv=PROJECTENV/env git+https://github.com/auzigog/django-template-heroku.git
    cd PROJECTNAME/code


## Usage
Usage information is available in `README.example.md`

## Checklist for starting a new project

  1) Edit `.env_local` to contain your local settings including your database connection string
  1) Rename `README.example.md` to `README.md` and replace with information for that project
  1)


## License
This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
