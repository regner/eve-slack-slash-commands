

import requests

from flask import abort
from urllib.parse import urljoin


def get_from_zkb(url):
    """Actually perform a request to zKB."""
    url = urljoin('https://zkillboard.com/', url)
    response = requests.get(url)
    
    if response.status_code == requests.codes.ok:
        return response.json()
    
    abort(504)


def get_zkb_character_search(character_name):
    """Looks up a given character name on the zKB autocomplete API."""
    url = urljoin('autocomplete/characterID/', str(character_name))
    return get_from_zkb(url)


def get_zkb_character_stats(character_id):
    """Looks up the stats for a given character ID."""
    url = urljoin('api/stats/characterID/', str(character_id))
    return get_from_zkb(url)

def get_zkb_corporation_search(corporation_name):
    """Looks up a given corporation name on the zKB autocomplete API."""
    url = urljoin('autocomplete/corporationID/', str(corporation_name))
    return get_from_zkb(url)


def get_zkb_corporation_stats(corporation_id):
    """Looks up the stats for a given corporation ID."""
    url = urljoin('api/stats/corporationID/', str(corporation_id))
    return get_from_zkb(url)


def get_zkb_type_search(type_name):
    """Looks up a given corporation name on the zKB autocomplete API."""
    url = urljoin('autocomplete/typeID/', str(type_name))
    return get_from_zkb(url)
