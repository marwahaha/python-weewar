import unittest
from weewar.api import *

class TestReadOnlyAPI(unittest.TestCase):
    
    """
    Test correct bahaviour of API calls.
    """
    
    BOGUS_USER_ID = '???'
    BOGUS_GAME_ID = '???'
    BOGUS_MAP_ID = '???'

    def test_missing_game(self):
        """
        Wrong game ID raises exception.
        """
        self.assertRaises(GameNotFound, game, self.BOGUS_GAME_ID)

    def test_missing_user(self):
        """
        Wrong user ID raises exception.
        """
        self.assertRaises(UserNotFound, user, self.BOGUS_USER_ID)
    
    def test_missing_map(self):
        """
        Wrong user ID raises exception.
        """
        self.assertRaises(MapNotFound, map_layout, self.BOGUS_MAP_ID)


if __name__ == '__main__':
    unittest.main()

