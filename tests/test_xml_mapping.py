import json
import unittest

from lxml import objectify
import os
import pytest

from weewar import ReadOnlyAPI, ELIZA

_here = os.path.dirname(os.path.abspath(__file__))

@pytest.mark.parametrize('method', [
    'open_games()',
    'all_users()',
    'headquarter()',
    'game(12345)',
    'user(12345)',
    'game_state(1234)',
    'map_layout(1234)',
])
def test_mapping(httpserver, monkeypatch, method):
    root = os.path.join(_here, 'mappings', method[0:method.index('(')])
    api = ELIZA()
    httpserver.serve_content(open(root + '.xml').read())
    monkeypatch.setattr(api, 'HOST', httpserver.url)
    response = eval('api.' + method)
    expected = json.load(open(root + '.json'))
    assert response == expected
