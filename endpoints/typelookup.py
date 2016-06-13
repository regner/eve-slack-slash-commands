

import eveimageserver

from flask_restful import Resource
from utils.slack import parse_slack_args
from utils.zkillboard import get_zkb_type_search


class TypeLookup(Resource):
    def post(self):
        """Searches zKB API for a given type and returns useful links."""
        args = parse_slack_args()

        search_name = args['text']
        search_results = get_zkb_type_search(search_name)

        if len(search_results) < 1:
            return {
                'response_type': 'in_channel',
                'color': '#36a64f',
                'text': 'No results could be found for the type {}.'.format(search_name),
                'fallback': 'No results could be found for the type {}.'.format(search_name),
            }

        eve_type = search_results[0]

        type_id = eve_type['id']
        type_name = eve_type['name']

        return {
            'response_type': 'in_channel',
            'attachments': [
                {
                    'fallback': type_name,
                    'title': type_name,
                    'thumb_url': eveimageserver.get_type_links(type_id)[64],
                    'mrkdwn_in': ['fields'],
                }
            ]
        }
