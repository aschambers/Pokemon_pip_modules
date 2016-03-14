import re
from setuptools import setup, find_packages


with open("README.rst", "rb") as f:
   long_descr = f.read().decode("utf-8")


setup(
   name = "awesome_pip_module",
   packages = find_packages(),
   entry_points = {
       "console_scripts": ['awesome_pip = awesome_pip_module.awesome_module:awesome_module']
       },
   version = "0.1.0",
   description = "Python command line html creator",
   long_description = long_descr,
   author = "Alan Schambers",
   author_email = "aschambers4291@gmail.com",
   url = "https://github.com/aschambers/awesome_pip_module"
)
