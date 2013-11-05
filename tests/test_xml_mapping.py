import unittest
from lxml import objectify
from weewar import ReadOnlyAPI, ELIZA


class TestXMLParsing(unittest.TestCase):

    """
    Test correct parsing of XML responses.
    """
    
    def setUp(self):
        self.api = ReadOnlyAPI()
        
    def parsed_xml(self, xml):
        return objectify.fromstring(xml.strip())
        
    def test_open_games(self):
        """
        XML response of open_games().
        """
        xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <games>
            <game id="182456" />
            <game id="182289" />
            <game id="182410" />
            <game id="181836" />
            <game id="182385" />
            <game id="182369" />
            <game id="182272" />
        </games>
        """
        expected = [182456, 182289, 182410, 181836, 182385, 182369, 182272]
        self.api._call_api = lambda a: self.parsed_xml(xml)
        self.assertEqual(self.api.open_games(), expected) 

    def test_all_users(self):
        """
        XML response of all_users().
        """
        xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <users>
            <user name="Watyousay" id="47874" rating="2213" />
            <user name="Stirling" id="26468" rating="2114" />
            <user name="ironcamel" id="1909" rating="2104" />
            <user name="Mr_Clean" id="17562" rating="2050" />
            <user name="elsirad" id="41192" rating="2050" />
            <user name="jeye" id="6101" rating="2049" />
            <user name="moJoe" id="4541" rating="2038" />
            <user name="Juffe" id="43710" rating="2037" />
            <user name="leelar" id="23263" rating="2018" />
            <user name="Doughnonuthin" id="39655" rating="2017" />
            <user name="General_Death" id="26235" rating="2001" />
            <user name="Riipperi" id="43711" rating="1989" />
            <user name="Aldairor" id="48371" rating="1968" />
        </users>
        """
        expected = [
            {'name': 'Watyousay', 'id': 47874, 'rating': 2213}, 
            {'name': 'Stirling', 'id': 26468, 'rating': 2114}, 
            {'name': 'ironcamel', 'id': 1909, 'rating': 2104}, 
            {'name': 'Mr_Clean', 'id': 17562, 'rating': 2050}, 
            {'name': 'elsirad', 'id': 41192, 'rating': 2050}, 
            {'name': 'jeye', 'id': 6101, 'rating': 2049}, 
            {'name': 'moJoe', 'id': 4541, 'rating': 2038}, 
            {'name': 'Juffe', 'id': 43710, 'rating': 2037}, 
            {'name': 'leelar', 'id': 23263, 'rating': 2018}, 
            {'name': 'Doughnonuthin', 'id': 39655, 'rating': 2017}, 
            {'name': 'General_Death', 'id': 26235, 'rating': 2001}, 
            {'name': 'Riipperi', 'id': 43711, 'rating': 1989}, 
            {'name': 'Aldairor', 'id': 48371, 'rating': 1968} 
        ]
        self.api._call_api = lambda a: self.parsed_xml(xml)
        self.assertEqual(self.api.all_users(), expected) 

    def test_game(self):
        """
        XML response of game().
        """
        xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <game id="21885">
          <id>21885</id>
          <name>Another short one</name>
          <round>36</round>
          <state>finished</state>
          <pendingInvites>false</pendingInvites>
          <pace>86400</pace>
          <type>Pro</type>
          <url>http://weewar.com/game/21885</url>
          <rated>true</rated>
          <since>12 hours</since>
          <players>
            <player index="0" current="true" result="victory">eviltwin</player>
            <player index="1" result="defeat">challenge</player>
          </players>
          <disabledUnitTypes>
            <type>Anti Aircraft</type>
            <type>Assault Artillery</type>
            <type>Battleship</type>
            <type>Bomber</type>
            <type>Destroyer</type>
            <type>Jet</type>
            <type>Helicopter</type>
            <type>Hovercraft</type>
            <type>Speedboat</type>
            <type>Submarine</type>
            <type>DFA</type>
            <type>Berserker</type>
          </disabledUnitTypes>
          <map>8</map>
          <mapUrl>http://weewar.com/map/8</mapUrl>
          <creditsPerBase>100</creditsPerBase>
          <initialCredits>300</initialCredits>
          <playingSince>Thu Jul 30 19:26:31 UTC 2009</playingSince>
        </game>
        """
        expected = {
            'id': 21885, 
            'name': 'Another short one', 
            'round': 36, 
            'state': 'finished', 
            'pendingInvites': False, 
            'pace': 86400, 
            'type': 'Pro', 
            'url': 'http://weewar.com/game/21885', 
            'rated': True, 
            'since': '12 hours', 
            'players': [
                {'index': 0,  
                 'current': True, 
                 'result': 'victory', 
                 'username': 'eviltwin'},
                {'index': 1,
                 'result': 'defeat',
                 'username': 'challenge'}],
            'disabledUnitTypes': [
                'Anti Aircraft', 
                'Assault Artillery', 
                'Battleship', 
                'Bomber', 
                'Destroyer', 
                'Jet', 
                'Helicopter', 
                'Hovercraft', 
                'Speedboat', 
                'Submarine', 
                'DFA', 
                'Berserker'],
            'map': 8, 
            'mapUrl': 'http://weewar.com/map/8', 
            'creditsPerBase': 100, 
            'initialCredits': 300, 
            'playingSince': 'Thu Jul 30 19:26:31 UTC 2009' 
        }
        self.api._call_api = lambda a: self.parsed_xml(xml)
        self.assertEqual(self.api.game(12345), expected) 

    def test_user(self):
        """
        XML response of user().
        """
        xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <user name="eviltwin" id="12903">
            <points>1531</points>
            <profile>http://weewar.com/user/eviltwin</profile>
            <draws>0</draws>
            <victories>2</victories>
            <losses>0</losses>
            <accountType>Basic</accountType>
            <on>false</on>
            <readyToPlay>false</readyToPlay>
            <gamesRunning>1</gamesRunning>
            <lastLogin>2009-07-30 18:12:13.0</lastLogin>
            <basesCaptured>12</basesCaptured>
            <creditsSpent>24750</creditsSpent>
            <favoriteUnits>
                <unit code="tank" />
                <unit code="heavyInfantry" />
                <unit code="lightInfantry" />
                <unit code="lightartillery" />
                <unit code="heavyartillery" />
                <unit code="lighttank" />
                <unit code="heavytank" />
            </favoriteUnits>
            <preferredPlayers />
            <games>
                <game name="Twins, Basil!">18682</game>
                <game name="Another short one">21885</game>
            </games>
            <maps />
        </user>
        """
        expected = {
            'name': 'eviltwin',
            'id': 12903,
            'points': 1531,
            'profile': 'http://weewar.com/user/eviltwin',
            'draws': 0,
            'victories': 2,
            'losses': 0,
            'accountType': 'Basic',
            'on': False,
            'readyToPlay': False, 
            'gamesRunning': 1, 
            'lastLogin': '2009-07-30 18:12:13.0', 
            'basesCaptured': 12, 
            'creditsSpent': 24750, 
            'favoriteUnits': [
                'tank', 
                'heavyInfantry', 
                'lightInfantry', 
                'lightartillery', 
                'heavyartillery', 
                'lighttank', 
                'heavytank'], 
            'preferredPlayers': [], 
            'games': [
                {'name': 'Twins, Basil!', 'id': 18682},
                {'name': 'Another short one', 'id': 21885}],
            'maps': []
        }
        self.api._call_api = lambda a: self.parsed_xml(xml)
        #compare(self.api.user(12345), expected) 
        self.assertEqual(self.api.user(12345), expected) 

    def test_latest_maps(self):
        """
        XML response of latest_maps().
        """
        xml = """
        <maps>
            <map id="42640">
                <name>Somar's first map</name>
                <initialCredits>1000</initialCredits>
                <perBaseCredits>10</perBaseCredits>
                <width>20</width>
                <height>10</height>
                <maxPlayers>2</maxPlayers>
                <url>http://weewar.com/map/42640</url>
                <thumbnail>http://weewar.com/images/maps/boardThumb_42640_ir1.png</thumbnail>
                <preview>http://weewar.com/images/maps/preview_42640_ir1.png</preview>
                <revision>2</revision>
                <creator>somar96</creator>
                <creatorProfile>http://weewar.com/user/somar96</creatorProfile>
            </map>
            <map id="42634">
                <name>Copy of Landing Point</name>
                <initialCredits>0</initialCredits>
                <perBaseCredits>300</perBaseCredits>
                <width>14</width>
                <height>14</height>
                <maxPlayers>2</maxPlayers>
                <url>http://weewar.com/map/42634</url>
                <thumbnail>http://weewar.com/images/maps/boardThumb_42634_ir2.png</thumbnail>
                <preview>http://weewar.com/images/maps/preview_42634_ir2.png</preview>
                <revision>2</revision>
                <creator>Shulgin</creator>
                <creatorProfile>http://weewar.com/user/Shulgin</creatorProfile>
            </map>
        </maps>
        """
        expected = [
            {
                'id': 42640,
                'name': "Somar's first map",
                'initialCredits': 1000, 
                'perBaseCredits': 10, 
                'width': 20, 
                'height': 10, 
                'maxPlayers': 2, 
                'url': 'http://weewar.com/map/42640', 
                'thumbnail': 'http://weewar.com/images/maps/boardThumb_42640_ir1.png', 
                'preview': 'http://weewar.com/images/maps/preview_42640_ir1.png', 
                'revision': 2, 
                'creator': 'somar96', 
                'creatorProfile': 'http://weewar.com/user/somar96'
            },
            {
                'id': 42634, 
                'name': 'Copy of Landing Point', 
                'initialCredits': 0, 
                'perBaseCredits': 300, 
                'width': 14, 
                'height': 14, 
                'maxPlayers': 2, 
                'url': 'http://weewar.com/map/42634', 
                'thumbnail': 'http://weewar.com/images/maps/boardThumb_42634_ir2.png', 
                'preview': 'http://weewar.com/images/maps/preview_42634_ir2.png', 
                'revision': 2, 
                'creator': 'Shulgin', 
                'creatorProfile': 'http://weewar.com/user/Shulgin'
            }
        ]
        self.api._call_api = lambda a: self.parsed_xml(xml)
        #for dict1, dict2 in zip(self.api.latest_maps(), expected):
        #    compare(dict1, dict2)
        self.assertEqual(self.api.latest_maps(), expected) 

    def test_headquarter(self):
        """
        XML response of headquarter().
        """
        xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <games>
            <game>
                <id>18682</id>
                <name>Twins, Basil!</name>
                <state>running</state>
                <since>3 minutes</since>
                <rated>true</rated>
                <link>http://weewar.com/game/18682</link>
                <url>http://weewar.com/game/18682</url>
                <map>1</map>
                <factionState>playing</factionState>
            </game>
            <game inNeedOfAttention="true">
                <id>21885</id>
                <name>Another short one</name>
                <state>finished</state>
                <result>victory</result>
                <since>17 hours 36 minutes</since>
                <rated>true</rated>
                <link>http://weewar.com/game/21885</link>
                <url>http://weewar.com/game/21885</url>
                <map>8</map>
                <factionState>finished</factionState>
            </game>
            <inNeedOfAttention>1</inNeedOfAttention>
        </games>
        """
        expected = (
            1, 
            [
                {
                    'id': 18682, 
                    'inNeedOfAttention': False, 
                    'name': 'Twins, Basil!', 
                    'state': 'running', 
                    'since': '3 minutes', 
                    'rated': True, 
                    'link': 'http://weewar.com/game/18682', 
                    'url': 'http://weewar.com/game/18682', 
                    'map': 1, 
                    'factionState': 'playing' 
                },
                {
                    'id': 21885, 
                    'inNeedOfAttention': True, 
                    'name': 'Another short one', 
                    'state': 'finished', 
                    'result': 'victory', 
                    'since': '17 hours 36 minutes', 
                    'rated': True, 
                    'link': 'http://weewar.com/game/21885', 
                    'url': 'http://weewar.com/game/21885', 
                    'map': 8, 
                    'factionState': 'finished'
                }
            ]
        )
        self.api._call_api = lambda a, b=None: self.parsed_xml(xml)
        self.assertEqual(self.api.headquarter(), expected) 

class TestELIZAMapping (TestXMLParsing):
    
    """
    Test correct parsing of XML responses for ELIZA API.
    """
    
    def setUp(self):
        self.api = ELIZA()
        
    def test_game_state(self):
        """
        Test game_state for correct XML parsing.
        """
        xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <game id="18682">
        <id>18682</id>
        <name>Twins, Basil!</name>
        <round>21</round>
        <state>finished</state>
        <pendingInvites>false</pendingInvites>
        <pace>259200</pace>
        <type>Pro</type>
        <url>http://weewar.com/game/18682</url>
        <rated>true</rated>
        <since>4 days 19 hours 34 minutes</since>
        <players>
            <player index="0" current="true" result="victory">eviltwin</player>
            <player index="1" result="votedout">thomas419</player>
        </players>
        <disabledUnitTypes>
            <type>Anti Aircraft</type>
            <type>Assault Artillery</type>
            <type>Battleship</type>
            <type>Bomber</type>
            <type>Destroyer</type>
            <type>Jet</type>
            <type>Helicopter</type>
            <type>Hovercraft</type>
            <type>Speedboat</type>
            <type>Submarine</type>
            <type>DFA</type>
            <type>Berserker</type>
        </disabledUnitTypes>
        <map>1</map>
        <mapUrl>http://weewar.com/map/1</mapUrl>
        <creditsPerBase>200</creditsPerBase>
        <initialCredits>100</initialCredits>
        <playingSince>Sat Aug 08 15:17:28 UTC 2009</playingSince>
        <factions>
            <faction current="true" credits="600" playerId="12903" playerName="eviltwin" state="finished" result="victory">
                <unit x="1" y="10" type="Light Artillery" quantity="7" finished="false" />
                <terrain x="1" y="10" type="Base" finished="false" />
            </faction>
            <faction playerId="12911" playerName="thomas419" state="finished" result="votedout">
                <unit x="2" y="10" type="Heavy Tank" quantity="4" finished="false" />
                <unit x="3" y="9" type="Tank" quantity="10" finished="false" />
                <unit x="3" y="11" type="Heavy Trooper" quantity="5" finished="false" />
                <unit x="4" y="10" type="Heavy Artillery" quantity="10" finished="false" />
                <unit x="5" y="9" type="Heavy Artillery" quantity="10" finished="false" />
                <unit x="5" y="10" type="Heavy Artillery" quantity="10" finished="false" />
                <unit x="5" y="11" type="Heavy Artillery" quantity="2" finished="false" />
                <unit x="6" y="8" type="Heavy Tank" quantity="7" finished="false" />
                <unit x="6" y="9" type="Heavy Tank" quantity="10" finished="false" />
                <unit x="6" y="10" type="Heavy Artillery" quantity="10" finished="false" />
                <unit x="6" y="11" type="Raider" quantity="10" finished="false" />
                <unit x="7" y="7" type="Raider" quantity="10" finished="false" />
                <unit x="7" y="8" type="Heavy Artillery" quantity="2" finished="false" />
                <unit x="7" y="12" type="Heavy Trooper" quantity="10" finished="false" />
                <unit x="8" y="8" type="Heavy Tank" quantity="10" finished="false" />
                <unit x="8" y="12" type="Heavy Tank" quantity="10" finished="false" />
                <unit x="8" y="13" type="Heavy Artillery" quantity="10" finished="false" />
                <unit x="9" y="11" type="Heavy Artillery" quantity="10" finished="false" />
                <unit x="10" y="5" type="Heavy Artillery" quantity="10" finished="false" />
                <unit x="10" y="6" type="Heavy Artillery" quantity="2" finished="false" />
                <unit x="10" y="7" type="Heavy Artillery" quantity="10" finished="false" />
                <unit x="10" y="10" type="Heavy Artillery" quantity="5" finished="false" />
                <unit x="11" y="9" type="Heavy Trooper" quantity="10" finished="false" />
                <terrain x="6" y="10" type="Base" finished="false" />
                <terrain x="7" y="6" type="Base" finished="false" />
                <terrain x="8" y="14" type="Base" finished="false" />
                <terrain x="9" y="9" type="Base" finished="false" />
                <terrain x="9" y="10" type="Base" finished="false" />
                <terrain x="10" y="10" type="Base" finished="false" />
                <terrain x="11" y="6" type="Base" finished="false" />
                <terrain x="11" y="13" type="Base" finished="false" />
                <terrain x="13" y="1" type="Base" finished="false" />
                <terrain x="13" y="9" type="Base" finished="false" />
                <terrain x="14" y="18" type="Base" finished="false" />
            </faction>
        </factions>
        </game>
        """
        expected = {
            'id': 18682,
            'name': 'Twins, Basil!',
            'round': 21,
            'state': 'finished',
            'pendingInvites': False,
            'pace': 259200,
            'type': 'Pro',
            'url': 'http://weewar.com/game/18682',
            'rated': True,
            'since': '4 days 19 hours 34 minutes',
            'players': [
                {
                    'index': 0, 
                    'current': True, 
                    'result': 'victory', 
                    'username': 'eviltwin'
                },
                {
                    'index': 1, 
                    'current': False, 
                    'result': 'votedout', 
                    'username': 'thomas419'
                }
            ],
            'disabledUnitTypes': [
                'Anti Aircraft', 'Assault Artillery', 'Battleship', 'Bomber', 
                'Destroyer', 'Jet', 'Helicopter', 'Hovercraft', 'Speedboat', 
                'Submarine', 'DFA', 'Berserker',
            ],
            'map': 1,
            'mapUrl': 'http://weewar.com/map/1', 
            'creditsPerBase': 200, 
            'initialCredits': 100, 
            'playingSince': 'Sat Aug 08 15:17:28 UTC 2009', 
            'factions': [
                {
                    'current': True,
                    'credits': 600,
                    'playerId': 12903,
                    'playerName': 'eviltwin',
                    'state': 'finished', 
                    'result': 'victory',
                    'units': [
                        {
                            'x': 1, 'y': 10, 
                            'type': 'Light Artillery', 
                            'quantity': 7,
                            'finished': False
                        }
                    ],
                    'terrain': [
                        {
                            'x': 1, 'y': 10,
                            'type': 'Base',
                            'finished': False
                        }
                    ]
                },
                {
                    'current': False,
                    'playerId': 12911,
                    'playerName': 'thomas419',
                    'state': 'finished', 
                    'result': 'votedout',
                    'units': [
                        {'x': 2, 'y': 10, 'type': 'Heavy Tank', 'quantity': 4, 'finished': False},
                        {'x': 3, 'y': 9, 'type': 'Tank', 'quantity': 10, 'finished': False},
                        {'x': 3, 'y': 11, 'type': 'Heavy Trooper', 'quantity': 5, 'finished': False},
                        {'x': 4, 'y': 10, 'type': 'Heavy Artillery', 'quantity': 10, 'finished': False},
                        {'x': 5, 'y': 9, 'type': 'Heavy Artillery', 'quantity': 10, 'finished': False},
                        {'x': 5, 'y': 10, 'type': 'Heavy Artillery', 'quantity': 10, 'finished': False},
                        {'x': 5, 'y': 11, 'type': 'Heavy Artillery', 'quantity': 2, 'finished': False},
                        {'x': 6, 'y': 8, 'type': 'Heavy Tank', 'quantity': 7, 'finished': False},
                        {'x': 6, 'y': 9, 'type': 'Heavy Tank', 'quantity': 10, 'finished': False},
                        {'x': 6, 'y': 10, 'type': 'Heavy Artillery', 'quantity': 10, 'finished': False},
                        {'x': 6, 'y': 11, 'type': 'Raider', 'quantity': 10, 'finished': False},
                        {'x': 7, 'y': 7, 'type': 'Raider', 'quantity': 10, 'finished': False},
                        {'x': 7, 'y': 8, 'type': 'Heavy Artillery', 'quantity': 2, 'finished': False},
                        {'x': 7, 'y': 12, 'type': 'Heavy Trooper', 'quantity': 10, 'finished': False},
                        {'x': 8, 'y': 8, 'type': 'Heavy Tank', 'quantity': 10, 'finished': False},
                        {'x': 8, 'y': 12, 'type': 'Heavy Tank', 'quantity': 10, 'finished': False},
                        {'x': 8, 'y': 13, 'type': 'Heavy Artillery', 'quantity': 10, 'finished': False},
                        {'x': 9, 'y': 11, 'type': 'Heavy Artillery', 'quantity': 10, 'finished': False},
                        {'x': 10, 'y': 5, 'type': 'Heavy Artillery', 'quantity': 10, 'finished': False},
                        {'x': 10, 'y': 6, 'type': 'Heavy Artillery', 'quantity': 2, 'finished': False},
                        {'x': 10, 'y': 7, 'type': 'Heavy Artillery', 'quantity': 10, 'finished': False},
                        {'x': 10, 'y': 10, 'type': 'Heavy Artillery', 'quantity': 5, 'finished': False},
                        {'x': 11, 'y': 9, 'type': 'Heavy Trooper', 'quantity': 10, 'finished': False},
                    ],
                    'terrain': [
                        {'x': 6, 'y': 10, 'type': 'Base', 'finished': False},
                        {'x': 7, 'y': 6, 'type': 'Base', 'finished': False},
                        {'x': 8, 'y': 14, 'type': 'Base', 'finished': False},
                        {'x': 9, 'y': 9, 'type': 'Base', 'finished': False},
                        {'x': 9, 'y': 10, 'type': 'Base', 'finished': False},
                        {'x': 10, 'y': 10, 'type': 'Base', 'finished': False},
                        {'x': 11, 'y': 6, 'type': 'Base', 'finished': False},
                        {'x': 11, 'y': 13, 'type': 'Base', 'finished': False},
                        {'x': 13, 'y': 1, 'type': 'Base', 'finished': False},
                        {'x': 13, 'y': 9, 'type': 'Base', 'finished': False},
                        {'x': 14, 'y': 18, 'type': 'Base', 'finished': False},
                    ]
                }
            ]
        }
        self.api._call_api = lambda a, b=None: self.parsed_xml(xml)
        self.assertEqual(self.api.game_state(1234), expected) 

    def test_map_layout(self):
        """
        Test map_layout for correct XML parsing.
        """
        xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <map id="8">
            <name>One on one</name>
            <initialCredits>300</initialCredits>
            <perBaseCredits>100</perBaseCredits>
            <width>22</width>
            <height>15</height>
            <maxPlayers>2</maxPlayers>
            <url>http://weewar.com/map/8</url>
            <thumbnail>http://weewar.com/images/maps/boardThumb_8_ir3.png</thumbnail>
            <preview>http://weewar.com/images/maps/preview_8_ir3.png</preview>
            <revision>2</revision>
            <creator>alex</creator>
            <creatorProfile>http://weewar.com/user/alex</creatorProfile>
            <terrains>
                <terrain x="0" y="7" type="Plains" />
                <terrain x="0" y="8" type="Woods" />
                <terrain x="0" y="9" type="Woods" />
                <terrain x="1" y="3" type="Plains" />
                <terrain x="1" y="5" type="Mountains" />
                <terrain x="1" y="6" type="Plains" />
                <terrain x="1" y="7" type="Woods" />
                <terrain x="1" y="8" type="Mountains" />
                <terrain x="1" y="9" type="Woods" />
                <terrain x="1" y="10" type="Woods" />
                <terrain x="2" y="3" type="Water" />
                <terrain x="2" y="4" type="Plains" />
                <terrain x="2" y="5" type="Plains" />
                <terrain x="2" y="6" type="Plains" />
                <terrain x="2" y="7" type="Plains" />
                <terrain x="2" y="8" type="Plains" />
                <terrain x="2" y="9" type="Plains" />
                <terrain x="2" y="10" type="Woods" />
                <terrain x="2" y="11" type="Woods" />
                <terrain x="3" y="2" type="Water" />
                <terrain x="3" y="3" type="Water" />
                <terrain x="3" y="4" type="Plains" />
                <terrain x="3" y="5" type="Plains" />
                <terrain x="3" y="6" type="Plains" />
                <terrain x="3" y="7" type="Plains" />
                <terrain startUnit="Trooper" startUnitOwner="1" startFaction="1" x="3" y="8" type="Base" />
                <terrain x="3" y="9" type="Mountains" />
                <terrain x="3" y="10" type="Woods" />
                <terrain x="3" y="11" type="Mountains" />
                <terrain x="3" y="12" type="Woods" />
                <terrain x="3" y="13" type="Woods" />
                <terrain x="4" y="2" type="Water" />
                <terrain x="4" y="3" type="Water" />
                <terrain x="4" y="4" type="Desert" />
                <terrain x="4" y="5" type="Plains" />
                <terrain x="4" y="6" type="Plains" />
                <terrain x="4" y="7" type="Plains" />
                <terrain x="4" y="8" type="Mountains" />
                <terrain x="4" y="9" type="Plains" />
                <terrain x="4" y="10" type="Plains" />
                <terrain x="4" y="11" type="Plains" />
                <terrain x="4" y="12" type="Mountains" />
                <terrain x="4" y="13" type="Woods" />
                <terrain x="5" y="2" type="Water" />
                <terrain x="5" y="3" type="Water" />
                <terrain x="5" y="4" type="Desert" />
                <terrain x="5" y="5" type="Desert" />
                <terrain x="5" y="6" type="Plains" />
                <terrain x="5" y="7" type="Plains" />
                <terrain x="5" y="8" type="Plains" />
                <terrain x="5" y="9" type="Plains" />
                <terrain x="5" y="10" type="Plains" />
                <terrain x="5" y="11" type="Plains" />
                <terrain x="5" y="12" type="Plains" />
                <terrain x="5" y="13" type="Plains" />
                <terrain x="5" y="14" type="Plains" />
                <terrain x="6" y="3" type="Water" />
                <terrain x="6" y="4" type="Water" />
                <terrain x="6" y="5" type="Desert" />
                <terrain x="6" y="6" type="Plains" />
                <terrain x="6" y="7" type="Plains" />
                <terrain x="6" y="8" type="Plains" />
                <terrain x="6" y="9" type="Plains" />
                <terrain x="6" y="10" type="Plains" />
                <terrain x="6" y="11" type="Plains" />
                <terrain x="6" y="12" type="Plains" />
                <terrain x="6" y="13" type="Plains" />
                <terrain x="6" y="14" type="Base" />
                <terrain x="7" y="2" type="Water" />
                <terrain x="7" y="3" type="Water" />
                <terrain x="7" y="4" type="Desert" />
                <terrain x="7" y="5" type="Plains" />
                <terrain x="7" y="6" type="Plains" />
                <terrain x="7" y="7" type="Plains" />
                <terrain x="7" y="8" type="Plains" />
                <terrain x="7" y="9" type="Plains" />
                <terrain x="7" y="10" type="Plains" />
                <terrain x="7" y="11" type="Plains" />
                <terrain x="7" y="12" type="Plains" />
                <terrain x="7" y="13" type="Plains" />
                <terrain x="7" y="14" type="Mountains" />
                <terrain x="8" y="1" type="Water" />
                <terrain x="8" y="2" type="Water" />
                <terrain x="8" y="3" type="Desert" />
                <terrain x="8" y="4" type="Desert" />
                <terrain x="8" y="5" type="Plains" />
                <terrain x="8" y="6" type="Plains" />
                <terrain x="8" y="7" type="Plains" />
                <terrain x="8" y="8" type="Plains" />
                <terrain x="8" y="9" type="Plains" />
                <terrain x="8" y="10" type="Plains" />
                <terrain x="8" y="11" type="Plains" />
                <terrain x="8" y="12" type="Plains" />
                <terrain x="8" y="13" type="Plains" />
                <terrain x="8" y="14" type="Plains" />
                <terrain x="9" y="0" type="Water" />
                <terrain x="9" y="1" type="Water" />
                <terrain x="9" y="2" type="Water" />
                <terrain x="9" y="3" type="Desert" />
                <terrain x="9" y="4" type="Water" />
                <terrain x="9" y="5" type="Water" />
                <terrain x="9" y="6" type="Plains" />
                <terrain x="9" y="7" type="Woods" />
                <terrain x="9" y="8" type="Plains" />
                <terrain x="9" y="9" type="Plains" />
                <terrain x="9" y="10" type="Plains" />
                <terrain x="9" y="11" type="Plains" />
                <terrain x="9" y="12" type="Plains" />
                <terrain x="9" y="13" type="Plains" />
                <terrain x="9" y="14" type="Mountains" />
                <terrain x="10" y="0" type="Water" />
                <terrain x="10" y="1" type="Desert" />
                <terrain x="10" y="2" type="Desert" />
                <terrain x="10" y="3" type="Plains" />
                <terrain x="10" y="4" type="Desert" />
                <terrain x="10" y="5" type="Water" />
                <terrain x="10" y="6" type="Desert" />
                <terrain x="10" y="7" type="Desert" />
                <terrain x="10" y="8" type="Woods" />
                <terrain x="10" y="9" type="Plains" />
                <terrain x="10" y="10" type="Plains" />
                <terrain x="10" y="11" type="Plains" />
                <terrain x="10" y="12" type="Plains" />
                <terrain startUnit="Trooper" startUnitOwner="1" startFaction="1" x="10" y="13" type="Base" />
                <terrain x="10" y="14" type="Desert" />
                <terrain x="11" y="0" type="Desert" />
                <terrain x="11" y="1" type="Plains" />
                <terrain x="11" y="2" type="Plains" />
                <terrain x="11" y="3" type="Mountains" />
                <terrain x="11" y="4" type="Plains" />
                <terrain x="11" y="5" type="Mountains" />
                <terrain x="11" y="6" type="Water" />
                <terrain x="11" y="7" type="Plains" />
                <terrain x="11" y="8" type="Plains" />
                <terrain x="11" y="9" type="Desert" />
                <terrain x="11" y="10" type="Mountains" />
                <terrain x="11" y="11" type="Desert" />
                <terrain x="11" y="12" type="Mountains" />
                <terrain x="11" y="13" type="Desert" />
                <terrain x="11" y="14" type="Desert" />
                <terrain x="12" y="0" type="Plains" />
                <terrain x="12" y="1" type="Plains" />
                <terrain startUnit="Trooper" startUnitOwner="0" startFaction="0" x="12" y="2" type="Base" />
                <terrain x="12" y="3" type="Plains" />
                <terrain x="12" y="4" type="Plains" />
                <terrain x="12" y="5" type="Plains" />
                <terrain x="12" y="6" type="Mountains" />
                <terrain x="12" y="7" type="Plains" />
                <terrain x="12" y="8" type="Plains" />
                <terrain x="12" y="9" type="Water" />
                <terrain x="12" y="10" type="Water" />
                <terrain x="12" y="11" type="Water" />
                <terrain x="12" y="12" type="Desert" />
                <terrain x="12" y="13" type="Water" />
                <terrain x="12" y="14" type="Water" />
                <terrain x="13" y="0" type="Mountains" />
                <terrain x="13" y="1" type="Plains" />
                <terrain x="13" y="2" type="Mountains" />
                <terrain x="13" y="3" type="Plains" />
                <terrain x="13" y="4" type="Plains" />
                <terrain x="13" y="5" type="Plains" />
                <terrain x="13" y="6" type="Plains" />
                <terrain x="13" y="7" type="Plains" />
                <terrain x="13" y="8" type="Woods" />
                <terrain x="13" y="9" type="Woods" />
                <terrain x="13" y="10" type="Desert" />
                <terrain x="13" y="11" type="Water" />
                <terrain x="13" y="12" type="Desert" />
                <terrain x="13" y="13" type="Water" />
                <terrain x="13" y="14" type="Water" />
                <terrain x="14" y="0" type="Mountains" />
                <terrain x="14" y="1" type="Plains" />
                <terrain x="14" y="2" type="Plains" />
                <terrain x="14" y="3" type="Plains" />
                <terrain x="14" y="4" type="Plains" />
                <terrain x="14" y="5" type="Plains" />
                <terrain x="14" y="6" type="Plains" />
                <terrain x="14" y="7" type="Plains" />
                <terrain x="14" y="8" type="Plains" />
                <terrain x="14" y="9" type="Plains" />
                <terrain x="14" y="10" type="Plains" />
                <terrain x="14" y="11" type="Desert" />
                <terrain x="14" y="12" type="Desert" />
                <terrain x="14" y="13" type="Water" />
                <terrain x="14" y="14" type="Water" />
                <terrain x="15" y="1" type="Plains" />
                <terrain x="15" y="2" type="Plains" />
                <terrain x="15" y="3" type="Plains" />
                <terrain x="15" y="4" type="Plains" />
                <terrain x="15" y="5" type="Plains" />
                <terrain x="15" y="6" type="Plains" />
                <terrain x="15" y="7" type="Plains" />
                <terrain x="15" y="8" type="Plains" />
                <terrain x="15" y="9" type="Plains" />
                <terrain x="15" y="10" type="Plains" />
                <terrain x="15" y="11" type="Plains" />
                <terrain x="15" y="12" type="Desert" />
                <terrain x="15" y="13" type="Water" />
                <terrain x="15" y="14" type="Water" />
                <terrain x="16" y="0" type="Base" />
                <terrain x="16" y="1" type="Plains" />
                <terrain x="16" y="2" type="Plains" />
                <terrain x="16" y="3" type="Plains" />
                <terrain x="16" y="4" type="Plains" />
                <terrain x="16" y="5" type="Plains" />
                <terrain x="16" y="6" type="Plains" />
                <terrain x="16" y="7" type="Plains" />
                <terrain x="16" y="8" type="Plains" />
                <terrain x="16" y="9" type="Plains" />
                <terrain x="16" y="10" type="Plains" />
                <terrain x="16" y="11" type="Desert" />
                <terrain x="16" y="12" type="Desert" />
                <terrain x="16" y="13" type="Water" />
                <terrain x="16" y="14" type="Water" />
                <terrain x="17" y="0" type="Mountains" />
                <terrain x="17" y="1" type="Plains" />
                <terrain x="17" y="2" type="Plains" />
                <terrain x="17" y="3" type="Plains" />
                <terrain x="17" y="4" type="Plains" />
                <terrain x="17" y="5" type="Plains" />
                <terrain x="17" y="6" type="Plains" />
                <terrain x="17" y="7" type="Plains" />
                <terrain x="17" y="8" type="Plains" />
                <terrain x="17" y="9" type="Plains" />
                <terrain x="17" y="10" type="Desert" />
                <terrain x="17" y="11" type="Water" />
                <terrain x="17" y="12" type="Water" />
                <terrain x="17" y="13" type="Water" />
                <terrain x="17" y="14" type="Water" />
                <terrain x="18" y="1" type="Plains" />
                <terrain x="18" y="2" type="Plains" />
                <terrain x="18" y="3" type="Mountains" />
                <terrain x="18" y="4" type="Plains" />
                <terrain x="18" y="5" type="Plains" />
                <terrain x="18" y="6" type="Plains" />
                <terrain x="18" y="7" type="Plains" />
                <terrain x="18" y="8" type="Plains" />
                <terrain x="18" y="9" type="Plains" />
                <terrain x="18" y="10" type="Plains" />
                <terrain x="18" y="11" type="Water" />
                <terrain x="18" y="12" type="Water" />
                <terrain x="18" y="13" type="Water" />
                <terrain x="19" y="0" type="Woods" />
                <terrain x="19" y="1" type="Woods" />
                <terrain x="19" y="2" type="Mountains" />
                <terrain startUnit="Trooper" startUnitOwner="0" startFaction="0" x="19" y="3" type="Base" />
                <terrain x="19" y="4" type="Plains" />
                <terrain x="19" y="5" type="Mountains" />
                <terrain x="19" y="6" type="Mountains" />
                <terrain x="19" y="7" type="Plains" />
                <terrain x="19" y="8" type="Plains" />
                <terrain x="19" y="9" type="Plains" />
                <terrain x="19" y="10" type="Plains" />
                <terrain x="19" y="11" type="Water" />
                <terrain x="19" y="12" type="Water" />
                <terrain x="20" y="0" type="Woods" />
                <terrain x="20" y="1" type="Woods" />
                <terrain x="20" y="2" type="Woods" />
                <terrain x="20" y="3" type="Mountains" />
                <terrain x="20" y="4" type="Plains" />
                <terrain x="20" y="5" type="Woods" />
                <terrain x="20" y="6" type="Plains" />
                <terrain x="20" y="7" type="Mountains" />
                <terrain x="20" y="8" type="Plains" />
                <terrain x="20" y="9" type="Mountains" />
                <terrain x="20" y="10" type="Plains" />
                <terrain x="20" y="11" type="Water" />
                <terrain x="20" y="12" type="Water" />
                <terrain x="21" y="2" type="Woods" />
                <terrain x="21" y="3" type="Woods" />
                <terrain x="21" y="4" type="Woods" />
                <terrain x="21" y="6" type="Woods" />
                <terrain x="21" y="7" type="Woods" />
                <terrain x="21" y="8" type="Plains" />
                <terrain x="21" y="10" type="Mountains" />
                <terrain x="21" y="11" type="Plains" />
                <terrain x="21" y="12" type="Water" />
            </terrains>
        </map>
        """
        expected = {
            'terrains': [
                {'y': 7, 'x': 0, 'type': 'Plains'}, 
                {'y': 8, 'x': 0, 'type': 'Woods'}, 
                {'y': 9, 'x': 0, 'type': 'Woods'}, 
                {'y': 3, 'x': 1, 'type': 'Plains'}, 
                {'y': 5, 'x': 1, 'type': 'Mountains'}, 
                {'y': 6, 'x': 1, 'type': 'Plains'}, 
                {'y': 7, 'x': 1, 'type': 'Woods'}, 
                {'y': 8, 'x': 1, 'type': 'Mountains'}, 
                {'y': 9, 'x': 1, 'type': 'Woods'}, 
                {'y': 10, 'x': 1, 'type': 'Woods'}, 
                {'y': 3, 'x': 2, 'type': 'Water'}, 
                {'y': 4, 'x': 2, 'type': 'Plains'}, 
                {'y': 5, 'x': 2, 'type': 'Plains'}, 
                {'y': 6, 'x': 2, 'type': 'Plains'}, 
                {'y': 7, 'x': 2, 'type': 'Plains'}, 
                {'y': 8, 'x': 2, 'type': 'Plains'}, 
                {'y': 9, 'x': 2, 'type': 'Plains'}, 
                {'y': 10, 'x': 2, 'type': 'Woods'}, 
                {'y': 11, 'x': 2, 'type': 'Woods'}, 
                {'y': 2, 'x': 3, 'type': 'Water'}, 
                {'y': 3, 'x': 3, 'type': 'Water'}, 
                {'y': 4, 'x': 3, 'type': 'Plains'}, 
                {'y': 5, 'x': 3, 'type': 'Plains'}, 
                {'y': 6, 'x': 3, 'type': 'Plains'}, 
                {'y': 7, 'x': 3, 'type': 'Plains'}, 
                {'startFaction': 1, 'startUnitOwner': '1', 'y': 8, 'x': 3, 'type': 'Base', 'startUnit': 'Trooper'}, 
                {'y': 9, 'x': 3, 'type': 'Mountains'}, 
                {'y': 10, 'x': 3, 'type': 'Woods'}, 
                {'y': 11, 'x': 3, 'type': 'Mountains'}, 
                {'y': 12, 'x': 3, 'type': 'Woods'}, 
                {'y': 13, 'x': 3, 'type': 'Woods'}, 
                {'y': 2, 'x': 4, 'type': 'Water'}, 
                {'y': 3, 'x': 4, 'type': 'Water'}, 
                {'y': 4, 'x': 4, 'type': 'Desert'}, 
                {'y': 5, 'x': 4, 'type': 'Plains'}, 
                {'y': 6, 'x': 4, 'type': 'Plains'}, 
                {'y': 7, 'x': 4, 'type': 'Plains'}, 
                {'y': 8, 'x': 4, 'type': 'Mountains'}, 
                {'y': 9, 'x': 4, 'type': 'Plains'}, 
                {'y': 10, 'x': 4, 'type': 'Plains'}, 
                {'y': 11, 'x': 4, 'type': 'Plains'}, 
                {'y': 12, 'x': 4, 'type': 'Mountains'}, 
                {'y': 13, 'x': 4, 'type': 'Woods'}, 
                {'y': 2, 'x': 5, 'type': 'Water'}, 
                {'y': 3, 'x': 5, 'type': 'Water'}, 
                {'y': 4, 'x': 5, 'type': 'Desert'}, 
                {'y': 5, 'x': 5, 'type': 'Desert'}, 
                {'y': 6, 'x': 5, 'type': 'Plains'}, 
                {'y': 7, 'x': 5, 'type': 'Plains'}, 
                {'y': 8, 'x': 5, 'type': 'Plains'}, 
                {'y': 9, 'x': 5, 'type': 'Plains'}, 
                {'y': 10, 'x': 5, 'type': 'Plains'}, 
                {'y': 11, 'x': 5, 'type': 'Plains'}, 
                {'y': 12, 'x': 5, 'type': 'Plains'}, 
                {'y': 13, 'x': 5, 'type': 'Plains'}, 
                {'y': 14, 'x': 5, 'type': 'Plains'}, 
                {'y': 3, 'x': 6, 'type': 'Water'}, 
                {'y': 4, 'x': 6, 'type': 'Water'}, 
                {'y': 5, 'x': 6, 'type': 'Desert'}, 
                {'y': 6, 'x': 6, 'type': 'Plains'}, 
                {'y': 7, 'x': 6, 'type': 'Plains'}, 
                {'y': 8, 'x': 6, 'type': 'Plains'}, 
                {'y': 9, 'x': 6, 'type': 'Plains'}, 
                {'y': 10, 'x': 6, 'type': 'Plains'}, 
                {'y': 11, 'x': 6, 'type': 'Plains'}, 
                {'y': 12, 'x': 6, 'type': 'Plains'}, 
                {'y': 13, 'x': 6, 'type': 'Plains'}, 
                {'y': 14, 'x': 6, 'type': 'Base'}, 
                {'y': 2, 'x': 7, 'type': 'Water'}, 
                {'y': 3, 'x': 7, 'type': 'Water'}, 
                {'y': 4, 'x': 7, 'type': 'Desert'}, 
                {'y': 5, 'x': 7, 'type': 'Plains'}, 
                {'y': 6, 'x': 7, 'type': 'Plains'}, 
                {'y': 7, 'x': 7, 'type': 'Plains'}, 
                {'y': 8, 'x': 7, 'type': 'Plains'}, 
                {'y': 9, 'x': 7, 'type': 'Plains'}, 
                {'y': 10, 'x': 7, 'type': 'Plains'}, 
                {'y': 11, 'x': 7, 'type': 'Plains'}, 
                {'y': 12, 'x': 7, 'type': 'Plains'}, 
                {'y': 13, 'x': 7, 'type': 'Plains'}, 
                {'y': 14, 'x': 7, 'type': 'Mountains'}, 
                {'y': 1, 'x': 8, 'type': 'Water'}, 
                {'y': 2, 'x': 8, 'type': 'Water'}, 
                {'y': 3, 'x': 8, 'type': 'Desert'}, 
                {'y': 4, 'x': 8, 'type': 'Desert'}, 
                {'y': 5, 'x': 8, 'type': 'Plains'}, 
                {'y': 6, 'x': 8, 'type': 'Plains'}, 
                {'y': 7, 'x': 8, 'type': 'Plains'}, 
                {'y': 8, 'x': 8, 'type': 'Plains'}, 
                {'y': 9, 'x': 8, 'type': 'Plains'}, 
                {'y': 10, 'x': 8, 'type': 'Plains'}, 
                {'y': 11, 'x': 8, 'type': 'Plains'}, 
                {'y': 12, 'x': 8, 'type': 'Plains'}, 
                {'y': 13, 'x': 8, 'type': 'Plains'}, 
                {'y': 14, 'x': 8, 'type': 'Plains'}, 
                {'y': 0, 'x': 9, 'type': 'Water'}, 
                {'y': 1, 'x': 9, 'type': 'Water'}, 
                {'y': 2, 'x': 9, 'type': 'Water'}, 
                {'y': 3, 'x': 9, 'type': 'Desert'}, 
                {'y': 4, 'x': 9, 'type': 'Water'}, 
                {'y': 5, 'x': 9, 'type': 'Water'}, 
                {'y': 6, 'x': 9, 'type': 'Plains'}, 
                {'y': 7, 'x': 9, 'type': 'Woods'}, 
                {'y': 8, 'x': 9, 'type': 'Plains'}, 
                {'y': 9, 'x': 9, 'type': 'Plains'}, 
                {'y': 10, 'x': 9, 'type': 'Plains'}, 
                {'y': 11, 'x': 9, 'type': 'Plains'}, 
                {'y': 12, 'x': 9, 'type': 'Plains'}, 
                {'y': 13, 'x': 9, 'type': 'Plains'}, 
                {'y': 14, 'x': 9, 'type': 'Mountains'}, 
                {'y': 0, 'x': 10, 'type': 'Water'}, 
                {'y': 1, 'x': 10, 'type': 'Desert'}, 
                {'y': 2, 'x': 10, 'type': 'Desert'}, 
                {'y': 3, 'x': 10, 'type': 'Plains'}, 
                {'y': 4, 'x': 10, 'type': 'Desert'}, 
                {'y': 5, 'x': 10, 'type': 'Water'}, 
                {'y': 6, 'x': 10, 'type': 'Desert'}, 
                {'y': 7, 'x': 10, 'type': 'Desert'}, 
                {'y': 8, 'x': 10, 'type': 'Woods'}, 
                {'y': 9, 'x': 10, 'type': 'Plains'}, 
                {'y': 10, 'x': 10, 'type': 'Plains'}, 
                {'y': 11, 'x': 10, 'type': 'Plains'}, 
                {'y': 12, 'x': 10, 'type': 'Plains'}, 
                {'startFaction': 1, 'startUnitOwner': '1', 'y': 13, 'x': 10, 'type': 'Base', 'startUnit': 'Trooper'}, 
                {'y': 14, 'x': 10, 'type': 'Desert'}, 
                {'y': 0, 'x': 11, 'type': 'Desert'}, 
                {'y': 1, 'x': 11, 'type': 'Plains'}, 
                {'y': 2, 'x': 11, 'type': 'Plains'}, 
                {'y': 3, 'x': 11, 'type': 'Mountains'}, 
                {'y': 4, 'x': 11, 'type': 'Plains'}, 
                {'y': 5, 'x': 11, 'type': 'Mountains'}, 
                {'y': 6, 'x': 11, 'type': 'Water'}, 
                {'y': 7, 'x': 11, 'type': 'Plains'}, 
                {'y': 8, 'x': 11, 'type': 'Plains'}, 
                {'y': 9, 'x': 11, 'type': 'Desert'}, 
                {'y': 10, 'x': 11, 'type': 'Mountains'}, 
                {'y': 11, 'x': 11, 'type': 'Desert'}, 
                {'y': 12, 'x': 11, 'type': 'Mountains'}, 
                {'y': 13, 'x': 11, 'type': 'Desert'}, 
                {'y': 14, 'x': 11, 'type': 'Desert'}, 
                {'y': 0, 'x': 12, 'type': 'Plains'}, 
                {'y': 1, 'x': 12, 'type': 'Plains'}, 
                {'startFaction': 0, 'startUnitOwner': '0', 'y': 2, 'x': 12, 'type': 'Base', 'startUnit': 'Trooper'}, 
                {'y': 3, 'x': 12, 'type': 'Plains'}, 
                {'y': 4, 'x': 12, 'type': 'Plains'}, 
                {'y': 5, 'x': 12, 'type': 'Plains'}, 
                {'y': 6, 'x': 12, 'type': 'Mountains'}, 
                {'y': 7, 'x': 12, 'type': 'Plains'}, 
                {'y': 8, 'x': 12, 'type': 'Plains'}, 
                {'y': 9, 'x': 12, 'type': 'Water'}, 
                {'y': 10, 'x': 12, 'type': 'Water'}, 
                {'y': 11, 'x': 12, 'type': 'Water'}, 
                {'y': 12, 'x': 12, 'type': 'Desert'}, 
                {'y': 13, 'x': 12, 'type': 'Water'}, 
                {'y': 14, 'x': 12, 'type': 'Water'}, 
                {'y': 0, 'x': 13, 'type': 'Mountains'}, 
                {'y': 1, 'x': 13, 'type': 'Plains'}, 
                {'y': 2, 'x': 13, 'type': 'Mountains'}, 
                {'y': 3, 'x': 13, 'type': 'Plains'}, 
                {'y': 4, 'x': 13, 'type': 'Plains'}, 
                {'y': 5, 'x': 13, 'type': 'Plains'}, 
                {'y': 6, 'x': 13, 'type': 'Plains'}, 
                {'y': 7, 'x': 13, 'type': 'Plains'}, 
                {'y': 8, 'x': 13, 'type': 'Woods'}, 
                {'y': 9, 'x': 13, 'type': 'Woods'}, 
                {'y': 10, 'x': 13, 'type': 'Desert'}, 
                {'y': 11, 'x': 13, 'type': 'Water'}, 
                {'y': 12, 'x': 13, 'type': 'Desert'}, 
                {'y': 13, 'x': 13, 'type': 'Water'}, 
                {'y': 14, 'x': 13, 'type': 'Water'}, 
                {'y': 0, 'x': 14, 'type': 'Mountains'}, 
                {'y': 1, 'x': 14, 'type': 'Plains'}, 
                {'y': 2, 'x': 14, 'type': 'Plains'}, 
                {'y': 3, 'x': 14, 'type': 'Plains'}, 
                {'y': 4, 'x': 14, 'type': 'Plains'}, 
                {'y': 5, 'x': 14, 'type': 'Plains'}, 
                {'y': 6, 'x': 14, 'type': 'Plains'}, 
                {'y': 7, 'x': 14, 'type': 'Plains'}, 
                {'y': 8, 'x': 14, 'type': 'Plains'}, 
                {'y': 9, 'x': 14, 'type': 'Plains'}, 
                {'y': 10, 'x': 14, 'type': 'Plains'}, 
                {'y': 11, 'x': 14, 'type': 'Desert'}, 
                {'y': 12, 'x': 14, 'type': 'Desert'}, 
                {'y': 13, 'x': 14, 'type': 'Water'}, 
                {'y': 14, 'x': 14, 'type': 'Water'}, 
                {'y': 1, 'x': 15, 'type': 'Plains'}, 
                {'y': 2, 'x': 15, 'type': 'Plains'}, 
                {'y': 3, 'x': 15, 'type': 'Plains'}, 
                {'y': 4, 'x': 15, 'type': 'Plains'}, 
                {'y': 5, 'x': 15, 'type': 'Plains'}, 
                {'y': 6, 'x': 15, 'type': 'Plains'}, 
                {'y': 7, 'x': 15, 'type': 'Plains'}, 
                {'y': 8, 'x': 15, 'type': 'Plains'}, 
                {'y': 9, 'x': 15, 'type': 'Plains'}, 
                {'y': 10, 'x': 15, 'type': 'Plains'}, 
                {'y': 11, 'x': 15, 'type': 'Plains'}, 
                {'y': 12, 'x': 15, 'type': 'Desert'}, 
                {'y': 13, 'x': 15, 'type': 'Water'}, 
                {'y': 14, 'x': 15, 'type': 'Water'}, 
                {'y': 0, 'x': 16, 'type': 'Base'}, 
                {'y': 1, 'x': 16, 'type': 'Plains'}, 
                {'y': 2, 'x': 16, 'type': 'Plains'}, 
                {'y': 3, 'x': 16, 'type': 'Plains'}, 
                {'y': 4, 'x': 16, 'type': 'Plains'}, 
                {'y': 5, 'x': 16, 'type': 'Plains'}, 
                {'y': 6, 'x': 16, 'type': 'Plains'}, 
                {'y': 7, 'x': 16, 'type': 'Plains'}, 
                {'y': 8, 'x': 16, 'type': 'Plains'}, 
                {'y': 9, 'x': 16, 'type': 'Plains'}, 
                {'y': 10, 'x': 16, 'type': 'Plains'}, 
                {'y': 11, 'x': 16, 'type': 'Desert'}, 
                {'y': 12, 'x': 16, 'type': 'Desert'}, 
                {'y': 13, 'x': 16, 'type': 'Water'}, 
                {'y': 14, 'x': 16, 'type': 'Water'}, 
                {'y': 0, 'x': 17, 'type': 'Mountains'}, 
                {'y': 1, 'x': 17, 'type': 'Plains'}, 
                {'y': 2, 'x': 17, 'type': 'Plains'}, 
                {'y': 3, 'x': 17, 'type': 'Plains'}, 
                {'y': 4, 'x': 17, 'type': 'Plains'}, 
                {'y': 5, 'x': 17, 'type': 'Plains'}, 
                {'y': 6, 'x': 17, 'type': 'Plains'}, 
                {'y': 7, 'x': 17, 'type': 'Plains'}, 
                {'y': 8, 'x': 17, 'type': 'Plains'}, 
                {'y': 9, 'x': 17, 'type': 'Plains'}, 
                {'y': 10, 'x': 17, 'type': 'Desert'}, 
                {'y': 11, 'x': 17, 'type': 'Water'}, 
                {'y': 12, 'x': 17, 'type': 'Water'}, 
                {'y': 13, 'x': 17, 'type': 'Water'}, 
                {'y': 14, 'x': 17, 'type': 'Water'}, 
                {'y': 1, 'x': 18, 'type': 'Plains'}, 
                {'y': 2, 'x': 18, 'type': 'Plains'}, 
                {'y': 3, 'x': 18, 'type': 'Mountains'}, 
                {'y': 4, 'x': 18, 'type': 'Plains'}, 
                {'y': 5, 'x': 18, 'type': 'Plains'}, 
                {'y': 6, 'x': 18, 'type': 'Plains'}, 
                {'y': 7, 'x': 18, 'type': 'Plains'}, 
                {'y': 8, 'x': 18, 'type': 'Plains'}, 
                {'y': 9, 'x': 18, 'type': 'Plains'}, 
                {'y': 10, 'x': 18, 'type': 'Plains'}, 
                {'y': 11, 'x': 18, 'type': 'Water'}, 
                {'y': 12, 'x': 18, 'type': 'Water'}, 
                {'y': 13, 'x': 18, 'type': 'Water'}, 
                {'y': 0, 'x': 19, 'type': 'Woods'}, 
                {'y': 1, 'x': 19, 'type': 'Woods'}, 
                {'y': 2, 'x': 19, 'type': 'Mountains'}, 
                {'startFaction': 0, 'startUnitOwner': '0', 'y': 3, 'x': 19, 'type': 'Base', 'startUnit': 'Trooper'}, 
                {'y': 4, 'x': 19, 'type': 'Plains'}, 
                {'y': 5, 'x': 19, 'type': 'Mountains'}, 
                {'y': 6, 'x': 19, 'type': 'Mountains'}, 
                {'y': 7, 'x': 19, 'type': 'Plains'}, 
                {'y': 8, 'x': 19, 'type': 'Plains'}, 
                {'y': 9, 'x': 19, 'type': 'Plains'}, 
                {'y': 10, 'x': 19, 'type': 'Plains'}, 
                {'y': 11, 'x': 19, 'type': 'Water'}, 
                {'y': 12, 'x': 19, 'type': 'Water'}, 
                {'y': 0, 'x': 20, 'type': 'Woods'}, 
                {'y': 1, 'x': 20, 'type': 'Woods'}, 
                {'y': 2, 'x': 20, 'type': 'Woods'}, 
                {'y': 3, 'x': 20, 'type': 'Mountains'}, 
                {'y': 4, 'x': 20, 'type': 'Plains'}, 
                {'y': 5, 'x': 20, 'type': 'Woods'}, 
                {'y': 6, 'x': 20, 'type': 'Plains'}, 
                {'y': 7, 'x': 20, 'type': 'Mountains'}, 
                {'y': 8, 'x': 20, 'type': 'Plains'}, 
                {'y': 9, 'x': 20, 'type': 'Mountains'}, 
                {'y': 10, 'x': 20, 'type': 'Plains'}, 
                {'y': 11, 'x': 20, 'type': 'Water'}, 
                {'y': 12, 'x': 20, 'type': 'Water'}, 
                {'y': 2, 'x': 21, 'type': 'Woods'}, 
                {'y': 3, 'x': 21, 'type': 'Woods'}, 
                {'y': 4, 'x': 21, 'type': 'Woods'}, 
                {'y': 6, 'x': 21, 'type': 'Woods'}, 
                {'y': 7, 'x': 21, 'type': 'Woods'}, 
                {'y': 8, 'x': 21, 'type': 'Plains'}, 
                {'y': 10, 'x': 21, 'type': 'Mountains'}, 
                {'y': 11, 'x': 21, 'type': 'Plains'}, 
                {'y': 12, 'x': 21, 'type': 'Water'}
            ], 
            'name': 'One on one', 
            'creator': 'alex', 
            'url': 'http://weewar.com/map/8', 
            'creatorProfile': 'http://weewar.com/user/alex', 
            'maxPlayers': 2, 
            'height': 15, 
            'width': 22, 
            'id': 8, 
            'perBaseCredits': 100, 
            'preview': 
            'http://weewar.com/images/maps/preview_8_ir3.png', 
            'initialCredits': 300, 
            'thumbnail': 'http://weewar.com/images/maps/boardThumb_8_ir3.png', 
            'revision': 2
        }
        self.api._call_api = lambda a, b=None: self.parsed_xml(xml)
        self.assertEqual(self.api.map_layout(1234), expected) 


def compare(dict1, dict2):
    keys = set(dict1.keys()) & set(dict2.keys())
    if set(dict1.keys()) != keys:
        print('missing in dict1:', list(set(dict1.keys()) - keys))
    if set(dict2.keys()) != keys:
        print('missing in dict2:', list(set(dict2.keys()) - keys))
    for key in keys:
        if dict1[key] != dict2[key]:
            print('__%s__\n  %r\n  %r' % (key, dict1[key], dict2[key]))

if __name__ == '__main__':
    unittest.main()

