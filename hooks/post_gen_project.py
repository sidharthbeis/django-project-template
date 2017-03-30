from __future__ import unicode_literals, absolute_import
# ACTIONS TO BE DONE AFTER THE PROJECT IS COMPLETED.
import os
import shutil
import random

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# Use the system PRNG if possible
try:
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False


def get_random_string(
        length=50,
        allowed_chars='abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)'):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    if using_sysrandom:
        return ''.join(random.choice(allowed_chars) for i in range(length))
    print(
        "Cookiecutter Django couldn't find a secure pseudo-random number generator on your system."
        " Please change change your SECRET_KEY variables in conf/settings/local.py and env.example"
        " manually."
    )
    return "CHANGEME!!"


def set_secret_key(setting_file_location):
    # Open locals.py
    with open(setting_file_location) as f:
        file_ = f.read()

    # Generate a SECRET_KEY that matches the Django standard
    SECRET_KEY = get_random_string()

    # Replace "CHANGEME!!!" with SECRET_KEY
    file_ = file_.replace('CHANGEME!!!', SECRET_KEY, 1)

    # Write the results to the locals.py module
    with open(setting_file_location, 'w') as f:
        f.write(file_)


def make_secret_key(project_directory):
    """Generates and saves random secret key"""
    # Determine the local_setting_file_location
    local_setting = os.path.join(
        project_directory,
        '{{cookiecutter.project_name}}/settings/common.py'
    )

    # local.py settings file
    set_secret_key(local_setting)

    env_file = os.path.join(
        project_directory,
        '.env.template'
    )

    # env.example file
    set_secret_key(env_file)

def remove_authentication_dir():
    """
    Removes directories related to authentication
    if it isn't going to be used
    """
    authentication_location = os.path.join(PROJECT_DIRECTORY, '{{cookiecutter.project_name}}/authentication')
    if os.path.exists(authentication_location):
        shutil.rmtree(authentication_location)


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def remove_heroku_files():
    """
    Removes files needed for heroku
    """
    filenames = ["Procfile", "runtime.txt"]
    for filename in filenames:
        file_name = os.path.join(PROJECT_DIRECTORY, filename)
        remove_file(file_name)


def remove_elasticbeanstalk():
    """
    Removes elastic beanstalk components
    """
    docs_dir_location = os.path.join(PROJECT_DIRECTORY, '.ebextensions')
    if os.path.exists(docs_dir_location):
        shutil.rmtree(docs_dir_location)

    filename = "ebsetenv.py"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def remove_travis_ci():
    """
    Removes travis-ci yml file
    """
    filename = ".travis.yml"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def remove_newrelic():
    """
    Removes Newrelic config file
    """
    filename = "{{cookiecutter.project_name}}/newrelic.ini"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def remove_circle_ci():
    """
    Removes circle-ci yml file
    """
    filename = "circle.yml"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def remove_celery():
    """
    Removes celery file
    """
    filename = "{{cookiecutter.project_name}}/celery.py"
    remove_file(os.path.join(
        PROJECT_DIRECTORY, filename
    ))


def perform_post_gen_action():
    """
    Performs actions needed after a Django project has been created.
    """
    # 1. Generates and saves random secret key
    make_secret_key(PROJECT_DIRECTORY)

    # Removes heroku files
    if '{{ cookiecutter.use_heroku }}'.lower() != 'y':
        remove_heroku_files()

    # Removes Elastic Beanstalk files
    if '{{ cookiecutter.use_elasticbeanstalk }}'.lower() != 'y':
        remove_elasticbeanstalk()

    # Removes travis-ci files
    if '{{ cookiecutter.use_travis_ci }}'.lower() != 'y':
        remove_travis_ci()

    # Removes travis-ci files
    if '{{ cookiecutter.use_circle_ci }}'.lower() != 'y':
        remove_circle_ci()

    # Removes newrelic files
    if '{{ cookiecutter.use_newrelic }}'.lower() != 'y':
        remove_newrelic()

    # Removes celery file if not required
    if '{{ cookiecutter.use_celery }}'.lower() != 'y':
        remove_celery()

    # Removes authentication folder if not required
    if '{{ cookiecutter.use_django_rest_framework_for_apis }}'.lower() != 'y':
        remove_authentication_dir()


if __name__ == "__main__":
    perform_post_gen_action()
