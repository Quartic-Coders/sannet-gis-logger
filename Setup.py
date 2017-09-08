import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "SannetLogger",
    version = "1.0.4",
    author = "Andrew Tangeman",
    author_email = "andrew@quarticsolutions.com",
    description = ("Standardize logging module for City of San Diego batch Processing."),
    license = "BSD",
    keywords = "cosd logger batch",
    #url = "http://packages.python.org/an_example_pypi_project",
    packages=['sannetlogger'],
)