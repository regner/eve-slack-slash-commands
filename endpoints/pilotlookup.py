

import eveimageserver

from flask_restful import Resource
from utils.slack import parse_slack_args
from utils.zkillboard import get_zkb_character_search, get_zkb_character_stats
from utils.misc import get_character_links


class PilotLookup(Resource):
    def post(self):
        """Searches zKB API for a given character and returns useful links."""
        args = parse_slack_args()
        
        search_name = args['text']
        search_results = get_zkb_character_search(search_name)
        
        if len(search_results) <1:
            return {
            'response_type': 'in_channel',
            'color': '#36a64f',
            'text': 'No results could be found for the character {}.'.format(search_name),
            'fallback': 'No results could be found for the character {}.'.format(search_name),
        }
        
        character = search_results[0]
        
        
        character_id = character['id']
        character_name = character['name']
        stats = get_zkb_character_stats(character_id)
        
        return {
            'response_type': 'in_channel',
            'attachments': [
                {
                    'fallback': character_name,
                    'title': character_name,
                    'thumb_url': eveimageserver.get_character_links(character_id)[64],
                    'mrkdwn_in': ['fields'],
                    'fields': [
                        {
                            'title': 'Kills',
                            'value': 'ISK: {:,d}\nShips: {:,d}\nPoints: {:,d}'.format(stats['iskDestroyed'], stats['shipsDestroyed'], stats['pointsDestroyed']),
                            'short': True,
                        },
                        {
                            'title': 'Losses',
                            'value': 'ISK: {:,d}\nShips: {:,d}\nPoints: {:,d}'.format(stats['iskLost'], stats['shipsLost'], stats['pointsLost']),
                            'short': True,
                        },
                        {
                            'title': 'Links',
                            'value': get_character_links(character_name, character_id),
                            'short': True,
                        },
                    ],
                }
            ]
        }