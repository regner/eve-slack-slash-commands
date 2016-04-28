

from flask_restful import reqparse


def parse_slack_args():
    parser = reqparse.RequestParser()
    parser.add_argument('team_id', type=str, required=True)
    parser.add_argument('user_id', type=str, required=True)
    parser.add_argument('channel_id', type=str, required=True)
    parser.add_argument('user_name', type=str, required=True)
    parser.add_argument('response_url', type=str, required=True)
    parser.add_argument('channel_name', type=str, required=True)
    parser.add_argument('command', type=str, required=True)
    parser.add_argument('token', type=str, required=True)
    parser.add_argument('team_domain', type=str, required=True)
    parser.add_argument('text', type=str, required=True)
    
    return parser.parse_args()