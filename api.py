#!/usr/bin/env python3.8

import requests
from collections import namedtuple
from typing import List
from typing import NamedTuple

Episode = namedtuple("Episode", ["category", "description", "id", "title", "url"])


def search_by_keyword(keyword: str) -> List[Episode]:
    URL = f"https://search.talkpython.fm/api/search?q={keyword}"

    episode_list = []

    with requests.Session() as session:
        resp = session.get(URL)

        if resp.status_code == 200:
            return [Episode(**episode) for episode in resp.json()["results"]]


"""
{
    'category': 'Episode',
    'description': 'As most of you know, learning to program opens '
               'doors. It takes every day people and turns them '
               'into creators. Once you know programming, and '
               "Python, you've passed through a door to a place "
               'with much more opportunity.',
    'id': 114,
    'title': 'Empowering developers at the Hidden Genius project',
    'url': '/episodes/show/114/empowering-developers-at-the-hidden-genius-project'
}
"""
