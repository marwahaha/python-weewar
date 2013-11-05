import os
import re
from setuptools import setup

_here = os.path.abspath(os.path.dirname(__file__))


def read(fname):
    return open(os.path.join(_here, fname)).read()


def version():
    """
    Extracts version from weewar.py to avoid having to import it.
    """
    weewar = open(os.path.join(_here, 'weewar.py')).read()
    m = re.search("^__version__ = '(\d+(?:\.\d+){1,2})'$", weewar, re.M)
    return m.group(1)


setup(
    name="python-weewar",
    version=version(),
    description="Python wrapper for the Weewar XML API",
    long_description=read('README'),
    author="Sebastian Rahlf",
    author_email="basti AT redtoad DOT de",
    url="http://bitbucket.org/basti/python-weewar/downloads/",
    license='lgpl',
    py_modules=['weewar'],
    install_requires=[
        'lxml>=2.1.5',
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Games/Entertainment :: Turn Based Strategy',
    ]

)
