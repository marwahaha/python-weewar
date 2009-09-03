from setuptools import setup
from weewar import VERSION, api

setup(
    name="python-weewar",
    version=VERSION,

    description="Python wrapper for the Weewar XML API",
    long_description=api.__doc__, 
    
    author="Sebastian Rahlf",
    author_email="basti AT redtoad DOT de",
    url="http://bitbucket.org/basti/python-weewar/downloads/",
    
    packages=['weewar'],
    install_requires=['lxml>=2.1.5'],
    
    classifiers=[
        'Development Status :: 3 - Alpha', 
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 
        'Programming Language :: Python :: 2.5', 
        'Programming Language :: Python :: 2.6', 
        'Topic :: Games/Entertainment :: Turn Based Strategy', 
    ]

)

