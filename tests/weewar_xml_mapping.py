import unittest
from lxml import objectify
from weewar.api import ReadOnlyAPI

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
            {'name' : 'Watyousay', 'id' : 47874, 'rating' : 2213}, 
            {'name' : 'Stirling', 'id' : 26468, 'rating' : 2114}, 
            {'name' : 'ironcamel', 'id' : 1909, 'rating' : 2104}, 
            {'name' : 'Mr_Clean', 'id' : 17562, 'rating' : 2050}, 
            {'name' : 'elsirad', 'id' : 41192, 'rating' : 2050}, 
            {'name' : 'jeye', 'id' : 6101, 'rating' : 2049}, 
            {'name' : 'moJoe', 'id' : 4541, 'rating' : 2038}, 
            {'name' : 'Juffe', 'id' : 43710, 'rating' : 2037}, 
            {'name' : 'leelar', 'id' : 23263, 'rating' : 2018}, 
            {'name' : 'Doughnonuthin', 'id' : 39655, 'rating' : 2017}, 
            {'name' : 'General_Death', 'id' : 26235, 'rating' : 2001}, 
            {'name' : 'Riipperi', 'id' : 43711, 'rating' : 1989}, 
            {'name' : 'Aldairor', 'id' : 48371, 'rating' : 1968} 
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
            'id' : 21885, 
            'name' : 'Another short one', 
            'round' : 36, 
            'state' : 'finished', 
            'pendingInvites' : False, 
            'pace' : 86400, 
            'type' : 'Pro', 
            'url' : 'http://weewar.com/game/21885', 
            'rated' : True, 
            'since' : '12 hours', 
            'players' : [
                {'index' : 0,  
                 'current' : True, 
                 'result' : 'victory', 
                 'username' : 'eviltwin'},
                {'index' : 1,
                 'result' : 'defeat',
                 'username' : 'challenge'}],
            'disabledUnitTypes' : [
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
            'map' : 8, 
            'mapUrl' : 'http://weewar.com/map/8', 
            'creditsPerBase' : 100, 
            'initialCredits' : 300, 
            'playingSince' : 'Thu Jul 30 19:26:31 UTC 2009' 
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
            'name' : 'eviltwin',
            'id' : 12903,
            'points' : 1531,
            'profile' : 'http://weewar.com/user/eviltwin',
            'draws' : 0,
            'victories' : 2,
            'losses' : 0,
            'accountType' : 'Basic',
            'on' : False,
            'readyToPlay' : False, 
            'gamesRunning' : 1, 
            'lastLogin' : '2009-07-30 18:12:13.0', 
            'basesCaptured' : 12, 
            'creditsSpent' : 24750, 
            'favoriteUnits' : [
                'tank', 
                'heavyInfantry', 
                'lightInfantry', 
                'lightartillery', 
                'heavyartillery', 
                'lighttank', 
                'heavytank'], 
            'preferredPlayers' : [], 
            'games' : [
                {'name' : 'Twins, Basil!', 'id' : 18682},
                {'name' : 'Another short one', 'id' : 21885}],
            'maps' : []
        }
        self.api._call_api = lambda a: self.parsed_xml(xml)
        #compare(self.api.user(12345), expected) 
        self.assertEqual(self.api.user(12345), expected) 

    def test_latest_maps(self):
        """
        XML response of test_latest_maps().
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
                'id' : 42640,
                'name' : "Somar's first map",
                'initialCredits' : 1000, 
                'perBaseCredits' : 10, 
                'width' : 20, 
                'height' : 10, 
                'maxPlayers' : 2, 
                'url' : 'http://weewar.com/map/42640', 
                'thumbnail' : 'http://weewar.com/images/maps/boardThumb_42640_ir1.png', 
                'preview' : 'http://weewar.com/images/maps/preview_42640_ir1.png', 
                'revision' : 2, 
                'creator' : 'somar96', 
                'creatorProfile' : 'http://weewar.com/user/somar96'
            },
            {
                'id' : 42634, 
                'name' : 'Copy of Landing Point', 
                'initialCredits' : 0, 
                'perBaseCredits' : 300, 
                'width' : 14, 
                'height' : 14, 
                'maxPlayers' : 2, 
                'url' : 'http://weewar.com/map/42634', 
                'thumbnail' : 'http://weewar.com/images/maps/boardThumb_42634_ir2.png', 
                'preview' : 'http://weewar.com/images/maps/preview_42634_ir2.png', 
                'revision' : 2, 
                'creator' : 'Shulgin', 
                'creatorProfile' : 'http://weewar.com/user/Shulgin'
            }
        ]
        self.api._call_api = lambda a: self.parsed_xml(xml)
        #for dict1, dict2 in zip(self.api.latest_maps(), expected):
        #    compare(dict1, dict2)
        self.assertEqual(self.api.latest_maps(), expected) 

def compare(dict1, dict2):
    keys = set(dict1.keys()) & set(dict2.keys())
    if set(dict1.keys()) != keys:
        print 'missing in dict1:', list(set(dict1.keys()) - keys)
    if set(dict2.keys()) != keys:
        print 'missing in dict2:', list(set(dict2.keys()) - keys)
    for key in keys:
        if dict1[key] != dict2[key]:
            print '[%r]: %r != %r' % (key, dict1[key], dict2[key])

if __name__ == '__main__':
    unittest.main()

