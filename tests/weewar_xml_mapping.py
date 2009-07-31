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


def compare(dict1, dict2):
    keys = set(dict1.keys()) & set(dict2.keys())
    if set(dict1.keys()) != keys:
        print 'missing in dict1:', list(set(dict1.keys()) - keys)
    if set(dict2.keys()) != keys:
        print 'missing in dict2:', list(set(dict1.keys()) - keys)
    for key in keys:
        if dict1[key] != dict2[key]:
            print '[%r]: %r != %r' % (key, dict1[key], dict2[key])

if __name__ == '__main__':
    unittest.main()

