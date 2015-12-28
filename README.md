# flask-skeleton

A "hello world" style Flask web server application that can be used to collect
and vend scientific data.

  1. [Flask](http://flask.pocoo.org/)
  2. [Flask-Restless](https://flask-restless.readthedocs.org/en/latest/)
  3. [Flask-Script](http://flask-script.readthedocs.org/en/latest/)

## development

Before you get started you'll need to have Python 2.6+ installed. After, you'll
need to also instal virtualenv. Research how to do this for whatever platform
you run before continuing.

### setup a virtualenv

Create a virtual environment the web application by running the following
commands in a terminal.

```bash
virtualenv my-venv
source my-venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python setup.py develop
```

### start the web server

Start the web server on your local machine using Flask-Manager.

```bash
./manage.py runserver
```

Then, in your browser, navigate to http://127.0.0.1:5000/ or
http://127.0.0.1:5000/data.

### stop the web server

To stop the web server, you'll need to push CTRL-C twice: once to kill the
worker, and again to kill the web application.
