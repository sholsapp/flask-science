#!/usr/bin/env python

import os

from setuptools import setup

README = None
with open(os.path.abspath('README.md')) as fh:
  README = fh.read()

setup(
  name='flask-science',
  version='0.0.1',
  description=README,
  author='Stephen Holsapple',
  author_email='sholsapp@gmail.com',
  url='http://www.flask.com',
  packages=['flaskscience'],
  install_requires=[
    'Flask>=0.10.1',
    'Flask-Script',
    'Flask-Restless',
  ],
)
