
"""
Wrapper for the Weewar XML Application Interface (API)
======================================================

Weewar provides 2 APIs: one read-only API for their players and a bot API
called ELIZA.  Further documentation on both is available at
http://weewar.wikispaces.com/api

Authentication
--------------
Some of the provided functions require a username and a password. Use your
Weewar account username and the API token accessible via
http://weewar.com/apiToken.

"""

from urllib2 import Request, urlopen, HTTPError
import base64
from lxml import etree
from lxml import objectify

__all__ = [
    'game', 'open_games', 'all_users', 'user', 'latest_maps', 'headquarter',
    'UserNotFound', 'GameNotFound', 
]

class ReadOnlyAPI (object):
    
    """
    The Read-only API provides the basic information on users and games.
    """

    def __init__(self, username=None, apikey=None):
        """
        Initialise API (with user credentials for authenticated calls).
        @param username: weewar username
        @type username: str
        @param apikey: Matching API key (from http://weewar.com/apiToken)
        @type apikey: str
        """
        self.username = username
        self.apikey = apikey

    def _call_api(self, url, authentication=False):
        """
        Calls the weewar API with authentication (if specified)
        """
        #print 'opening %s...' % url
        req = Request(url)

        if authentication and self.username is not None:
            base64string = base64.encodestring(
                '%s:%s' % (self.username, self.apikey))[:-1]
            req.add_header("Authorization", "Basic %s" % base64string)

        handle = urlopen(req)
        return objectify.parse(handle).getroot()
        #xml = handle.read()
        #print xml
        #return objectify.fromstring(xml)

    # Access specific games
    URL_GAME = 'http://weewar.com/api/game/%s'

    def game(self, id):
        """
        Returns the status of a game and gives information about the
        participating players.
        """
        try:
            root = self._call_api(self.URL_GAME % id)
            return self._parse_game(root)
        except HTTPError, e:
            if e.code==404:
                raise GameNotFound(id)
            else:
                raise

    # Access all open games
    URL_OPEN_GAMES = 'http://weewar.com/api1/games/open'

    def open_games(self):
        """
        Returns all currently available open games.
        """
        # <games>
        #   <game id="181887" />
        #   ...
        # </games>
        root = self._call_api(self.URL_OPEN_GAMES)
        return [int(child.get('id'))
                for child in root.findall('game')]

    # Access a list of users
    URL_ALL_USERS = 'http://weewar.com/api1/users/all'

    def all_users(self):
        """
        Returns a list of all users who have been online in the last 7 days,
        including their current ranking.
        """
        root = self._call_api(self.URL_ALL_USERS)
        # <users>
        #   <user name="wulendam" id="21149" rating="1416" />
        #   ...
        # </users>
        return [
            dict(id=int(child.get('id')), 
                 name=child.get('name'), 
                 rating=int(child.get('rating'))) 
            for child in root.findall('user')
        ]

    # Access a single user
    URL_USER = 'http://weewar.com/api1/user/%s'

    def user(self, username):
        """
        Returns detailed information about a single user, including everything
        that is visible on the profile page and the games the user is
        participating in.
        """
        try:
            root = self._call_api(self.URL_USER % username)
            return self._parse_user(root)
        except HTTPError, e:
            if e.code==404:
                raise UserNotFound(username)
            else:
                raise

    # Access the latest maps
    URL_LATEST_MAPS = 'http://weewar.com/api1/maps'

    def latest_maps(self):
        """
        Returns the latest published maps including urls for previews, images,
        and other details.
        """
        root = self._call_api(self.URL_LATEST_MAPS)
        return map(self._parse_map, root.findall('map'))

    # Access your headquarters
    URL_HEADQUARTER = 'http://weewar.com/api1/headquarters'

    def headquarter(self):
        """
        Returns all games that are listed in your Headquarters. Includes
        information about the id, the url, the state, and the name of the game.
        An attribute is added if the game is in need of attention, e.g: its the
        users turn or the game is not yet started or the user is invited to
        this game.
        """
        root = self._call_api(self.URL_HEADQUARTER, True)
        need_attention = root.inNeedOfAttention
        
        # <game>
        #   <id>181897</id>
        #   <name>Stirling's Aruba</name>
        #   <state>running</state>
        #   <since>54 minutes</since>
        #   <rated>false</rated>
        #   <link>http://weewar.com/game/181897</link>
        #   <url>http://weewar.com/game/181897</url>
        #   <map>38297</map>
        #   <factionState>playing</factionState>
        # </game>
        games = [dict(
            (child.tag, child.pyval) 
            for child in game.iterchildren())
            for game in root.findall('game')]
        return need_attention, games

    def _parse_game(self, node):
        """
        Returns a simple dict for a game node.
        Example XML::

            <game id="181897">
                <id>181897</id>
                <name>Stirling's Aruba</name>
                <round>1</round>
                <state>running</state>
                <pendingInvites>true</pendingInvites>
                <pace>86400</pace>
                <type>Basic</type>
                <url>http://weewar.com/game/181897</url>
                <rated>false</rated>
                <since>1 hour 52 minutes</since>
                <players>
                    <player index="0">basti688</player>
                </players>
                <disabledUnitTypes>
                    <type>Hovercraft</type>
                    <type>Battleship</type>
                </disabledUnitTypes>
                <map>38297</map>
                <mapUrl>http://weewar.com/map/38297</mapUrl>
                <creditsPerBase>100</creditsPerBase>
                <initialCredits>300</initialCredits>
                <playingSince>Wed Jul 29 11:00:56 UTC 2009</playingSince>
            </game>

        """
        # these nodes have attributes
        # or childnodes
        complex_types = [
            'players', 
            'disabledUnitTypes'
        ]
        values = dict(
            (child.tag, child.pyval) 
            for child in node.iterchildren()
            if child.tag not in complex_types
        )
        #values['id'] = node.get('id')
        def _attrs(node, required, optional=None):
            attrs = {}
            for attr, type_ in required.items():
                try:
                    if type_ == bool:
                        attrs[attr] = node.get(attr).lower()=='true'
                    else:
                        attrs[attr] = type_(node.get(attr))
                except AttributeError:
                    attrs[attr] = node.get(attr)
            if optional:
                for attr, type_ in optional.items():
                    try:
                        if type_ == bool:
                            attrs[attr] = node.get(attr).lower()=='true'
                        else:
                            attrs[attr] = type_(node.get(attr))
                    except AttributeError:
                        pass
            return attrs
        values['players'] = [
            dict(username=player, 
                 **_attrs(player, {'index' : int, 'result' : str}, 
                          {'current' : bool}))
            for player in node.players.iterchildren()
        ]
        values['disabledUnitTypes'] = node.disabledUnitTypes.findall('type')
        return values

    def _parse_map(self, node):
        """
        Returns a simple dict for a map node.
        Example XML::

            <maps>
                <map id="42552">
                    <name>Trench Warfare - Balanced</name>
                    <initialCredits>200</initialCredits>
                    <perBaseCredits>100</perBaseCredits>
                    <width>30</width>
                    <height>10</height>
                    <maxPlayers>2</maxPlayers>
                    <url>http://weewar.com/map/42552</url>
                    <thumbnail>http://weewar.com/images/maps/boardThumb_42552_ir2.png</thumbnail>
                    <preview>http://weewar.com/images/maps/preview_42552_ir2.png</preview>
                    <revision>2</revision>
                    <creator>General_Death</creator>
                    <creatorProfile>http://weewar.com/user/General_Death</creatorProfile>
                </map>
                ...
            </maps>

        """
        values = dict((child.tag, child.pyval) 
                      for child in node.iterchildren())
        values['id'] = int(node.get('id'))
        return values

    def _parse_user(self, node):
        """
        Returns a simple dict for a user node.
        Example XML::

            <?xml version="1.0" encoding="UTF-8"?>
            <user name="basti688" id="12918">
                <points>1500</points>
                <profile>http://weewar.com/user/basti688</profile>
                <draws>0</draws>
                <victories>0</victories>
                <losses>0</losses>
                <accountType>Basic</accountType>
                <on>false</on>
                <readyToPlay>false</readyToPlay>
                <gamesRunning>1</gamesRunning>
                <lastLogin>2009-07-29 10:55:46.0</lastLogin>
                <basesCaptured>0</basesCaptured>
                <creditsSpent>200</creditsSpent>
                <favoriteUnits>
                    <unit code="lighttank" />
                </favoriteUnits>
                <preferredPlayers>
                    <player name="EgoBruiser" id="35086" />
                    <player name="bobbob" id="25808" />
                    <player name="MerissaofBulb" id="39154" />
                </preferredPlayers>
                <games>
                    <game name="game?">173101</game>
                    <game name="This is going to be long">169581</game>
                </games>
                <maps>
                    <map>36991</map>
                    <map>42196</map>
                    <map>42317</map>
                </maps>
            </user>
        """
        # these nodes have attributes
        # or childnodes
        complex_types = [
            'favoriteUnits', 
            'games', 
            'maps', 
            'preferredPlayers', 
            'disabledUnitTypes'
        ]
        values = dict(
            (child.tag, child.pyval) 
            for child in node.iterchildren()
            if child.tag not in complex_types
        )
        values['name'] = node.get('name')
        values['id'] = int(node.get('id'))
        values['games'] = [
            dict(id=child.pyval, name=child.get('name')) 
            for child in node.games.iterchildren()
            if child.tag == 'game'
        ]
        values['favoriteUnits'] = [
            child.get('code') 
            for child in node.favoriteUnits.iterchildren()
            if child.tag == 'unit'
        ]
        values['preferredPlayers'] = [
            dict(id=child.get('id'), name=child.get('name')) 
            for child in node.preferredPlayers.iterchildren()
            if child.tag == 'player'
        ]
        values['maps'] = [child.pyval
            for child in node.maps.iterchildren()
            if child.tag == 'map'
        ]
        return values 


class ELIZA (ReadOnlyAPI):

    """
    Weewar Bot-API (ELIZA)
    ======================

    In order for ELIZA to accept request the username MUST start with "ai_"
    This is so bots are recognizable by the community as such.

    You can not register a user name with a "_" in it at the moment, however
    you can change the name in your settings after the initial registration to
    comply with the Eliza requirements. The registration process will soon be
    fixed accordingly.
    """

    URL_GAME_STATE = 'http://weewar.com/api1/gamestate/%s'

    def game_state(self, id):
        """
        """

class UserNotFound (Exception):
    """
    The specified weewar game could not be found.
    """

class GameNotFound (Exception):
    """
    The specified weewar game could not be found.
    """

def game(id):
    """
    Returns the status of a game and gives information about the participating
    players.
    @param id: Unique ID of weewar game.
    @type id: int
    @rtype: dict
    """
    api = ReadOnlyAPI()
    return api.game(id)
    
def open_games():
    """
    Returns all currently available open games as a list of IDs.
    @rtype: [int]
    """
    api = ReadOnlyAPI()
    return api.open_games()
    
def all_users():
    """
    Returns a list of all users who have been online in the last 7 days,
    including their current ranking.
    @rtype: dict
    """
    api = ReadOnlyAPI()
    return api.all_users()
    
def user(username):
    """
    Returns detailed information about a single user, including everything that
    is visible on the profile page and the games the user is participating in.
    @param unsername: Unique unsername of weewar player.
    @type id: str
    @rtype: dict
    """
    api = ReadOnlyAPI()
    return api.user(username)

def latest_maps():
    """
    Returns the latest published maps including urls for previews, images, and
    other details.
    @rtype: dict
    """
    api = ReadOnlyAPI()
    return api.latest_maps()
    
def headquarter(username, apikey):
    """
    Returns all games that are listed in your Headquarters. Includes
    information about the id, the url, the state, and the name of the game.  An
    attribute is added if the game is in need of attention, e.g: its the users
    turn or the game is not yet started or the user is invited to this game.
    @param username: weewar username
    @type username: str
    @param apikey: Matching API key (from http://weewar.com/apiToken)
    @type apikey: str
    @return: A tuple containing (<games in need of attention>, [<game info>])
    @rtype: (int, [dict, ...])
    """
    api = ReadOnlyAPI(username, apikey)
    return api.headquarter()
    
#if __name__ == '__main__':
#    print open_games()
#    print all_users()
#    u = user('eviltwin')
#    print 'User %(name)s (%(points)s points)' % u,
#    print 'has %i games:' % len(u['games'])
#    for g in u['games']:
#        print ' - %(name)s (%(url)s)' % game(g['id'])
#    print latest_maps()
#    print headquarter('eviltwin', '...')
