# coding: utf-8

from setuptools import setup

PACKAGE = "dutils"
NAME = "Django Utils"
DESCRIPTION = "Django common utils"
AUTHOR = "runforever"
AUTHOR_EMAIL = "c.chenchao.c@gmail.com"
URL = "runforever.github.io"
VERSION = '0.1'


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=[
        'dutils',
    ],
    install_requires=[
        'pymongo',
        'django',
    ],
    zip_safe=False,
)
