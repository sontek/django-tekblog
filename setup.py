import os
from setuptools import setup, find_packages

from tekblog import VERSION


f = open(os.path.join(os.path.dirname(__file__), 'README'))
readme = f.read()
f.close()

setup(
    name='django-tekblog',
    version='0.1.3',
    description='django-tekblog is a reusable Django application for simple blogging.',
    long_description=readme,
    author='sontek',
    author_email='sontek@gmail.com',
    url='http://github.com/sontek/django-tekblog/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
