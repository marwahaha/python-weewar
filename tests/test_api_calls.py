
"""
Test correct behaviour of API calls.
"""

import pytest
import weewar


BOGUS_USER_ID = '???'
BOGUS_GAME_ID = '???'
BOGUS_MAP_ID = '???'


def test_missing_game_raises_exception():
    """
    Wrong game ID raises exception.
    """
    pytest.raises(weewar.GameNotFound, weewar.game, BOGUS_GAME_ID)


def test_missing_user_raises_exception():
    """
    Wrong user ID raises exception.
    """
    pytest.raises(weewar.UserNotFound, weewar.user, BOGUS_USER_ID)


def test_missing_map_raises_exception():
    """
    Wrong user ID raises exception.
    """
    pytest.raises(weewar.MapNotFound, weewar.map_layout, BOGUS_MAP_ID)

