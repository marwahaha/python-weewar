import unittest
from lxml import objectify
from weewar.api import ReadOnlyAPI

class TestSequenceFunctions(unittest.TestCase):

    """
    """
    
    def setUp(self):
        self.api = ReadOnlyAPI()
        
    def parsed_xml(self, xml):
        return objectify.fromstring(xml.strip())
        
    def test_game(self):
        """
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

if __name__ == '__main__':
    unittest.main()

