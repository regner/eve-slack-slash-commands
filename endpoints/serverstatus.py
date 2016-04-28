

from flask_restful import Resource
from utils.slack import parse_slack_args
from utils.server import convert_server_name, get_server_status, get_all_server_status


class ServerStatus(Resource):
    def post(self):
        """Retrieves the status of EVE Online servers."""
        args = parse_slack_args()

        server_name = args['text'].lower()
        if server_name == '':
            server_name = convert_server_name('tq')
            fields = [get_server_status(server_name)]
        
        elif server_name == 'all':
            fields = get_all_server_status()

        else:
            server_name = convert_server_name(server_name)
            fields = [get_server_status(server_name)]

        return {
            'response_type': 'in_channel',
            'attachments': [
                {
                    'fallback': ' | '.join(['{} ({})'.format(field['title'], field['value']) for field in fields]),
                    'pretext': 'Server status: {}'.format(server_name.capitalize()),
                    'fields': fields,
                    'mrkdwn_in': ['fields'],
                }
            ]
        }
