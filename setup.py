# coding: utf-8

from setuptools import setup

PACKAGE = "djangoutils"
NAME = "Django Utils"
DESCRIPTION = "Django common utils"
AUTHOR = "runforever"
AUTHOR_EMAIL = "c.chenchao.c@gmail.com"
URL = "runforever.github.io"
VERSION = '0.1'


setup(
    Name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=[
        'djangoutils',
    ],
    install_requires=[
        'pymongo',
        'django',
    ],
    zip_safe=False,
)
