Production ready starter template for Django Projects running on AWS Elastic Beanstalk

## Features
* Django 1.10.x
* Whitenoise for static files
* Configuration via environment variables using dj_database_url and dj_email_url
* Sane logging defaults
* Using pip-tools to pin requirements.in / requirements.txt
* MySQL or Postgres for database
* Optional support for Celery
* Optional support for TravisCI and CircleCI
* Optional support for Heroku and AWS Elastic Beanstalk
* Optional support for NewRelic and LogEntries
* Optional support for Django Rest Framework


## Quick Start

Install [cookiecutter](https://github.com/audreyr/cookiecutter) globally (not in a virtualenv):
```bash
pip install cookiecutter --user
```

Run cookiecutter in your `apps` directory:
```bash
cookiecutter https://github.com/hashedin/django-project-template -f
```

Cookiecutter creates a new directory for your app, `cd` into that directory.

Create a virtualenv:
```bash
virtualenv .venv
source .venv/bin/activate
```

Upgrade pip
```bash
pip install --upgrade pip
```

Install requirements.txt
```bash
pip install -r requirements/local.txt
```

Commit the source code to git
```bash
git init .
git add -A 
git commit -m "Initial Commit using django-project-template"
```

At this point, your Django project is ready.


## Re-running Cookie Cutter
Let's say you started your project, and now there are additional updates to django-project-template. Or, you had disabled celery, but now want to enable support. How do you incorporate those changes to your existing project, where you have already written some code?

 1. First, make sure commit all your changes to git. For safety, push it to a remote git server
 1. Then, re-run cookiecutter with the `-f` flag, perhaps with different settings. Note that you must be in the `apps` directory and must type in the exact same repository and project name - otherwise cookiecutter will create new directories.
 1. Use `git status` and `git diff` and carefully review the changes
 1. If there are conflicts, manually merge them
 1. If satisfied, commit the changes. If not, revert and re-try with different cookiecutter settings
 
