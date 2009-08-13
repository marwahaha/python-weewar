from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name="python-weewar",
    version="0.2",

    description="Python wrapper for the Weewar XML API",
    long_description="""\
Python wrapper for the Weewar XML API
=====================================

Weewar (http://weewar.com) is an "Award winning turn based multiplayer strategy
game". Apart from being highly addictive, it provides 2 APIs: one read-only API
for players and a bot API called ELIZA (further documentation on both is
available at http://weewar.wikispaces.com/api) . 

This module aims enables you to conveniently call each of these API functions
from within your python script.

Available API calls
-------------------

The following functions are supplied:

 - game(id) returns the status of a game and gives information about the
   participating players.
    
 - open_games() returns all currently available open games as a list of IDs.
    
 - all_users() returns a list of all users who have been online in the last 7
   days, including their current ranking.
    
 - user(username) Returns detailed information about a single user, including
   everything that is visible on the profile page and the games the user is
   participating in.

 - latest_maps() returns the latest published maps including urls for previews,
   images, and other details.
    
 - headquarter(username, apikey) returns all games that are listed in your
   Headquarters. Includes information about the id, the url, the state, and the
   name of the game.  An attribute is added if the game is in need of
   attention, e.g: its the users turn or the game is not yet started or the
   user is invited to this game (requires authentication).

 - game_state(username, apikey, id) offers more information about the state of
   a game (requires authentication).

 - map_layout(id) returns complete map layout.

Authentication
--------------

Some of the provided functions require a username and a password. Use your
Weewar account username and the API token accessible via
http://weewar.com/apiToken.

What's still missing?
---------------------

At the moment support for commands still needs to be implemented.
""",
    
    author="Sebastian Rahlf",
    author_email="basti AT redtoad DOT de",
    url="http://bitbucket.org/basti/python-weewar/",
    
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

