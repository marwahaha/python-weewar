from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name="python-weewar",
    version="0.1dev",

    description="Python wrapper for the Weewar XML API",
    long_description="""\
""",
    
    author="Sebastian Rahlf",
    author_email="basti AT redtoad DOT de",
    url="http://bitbucket.org/basti/python-weewar/",
    
    packages=['weewar'],
    install_requires=['lxml>=2.1.5']
)

