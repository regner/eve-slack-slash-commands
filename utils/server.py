

import requests

from flask import abort


eve_servers = {
    'tranquility': 'https://crest-tq.eveonline.com',
    'singularity': 'https://api-sisi.testeveonline.com',
    'duality': 'https://api-duality.testeveonline.com',
    # TODO: Add Osmosis
}

eve_servers_name_map = {
    'tq': 'tranquility',
    'sisi': 'singularity',
}


def convert_server_name(server_name):
    """Converts common server names to what we use in our mappings."""
    if server_name in eve_servers.keys():
        return server_name

    if server_name in eve_servers_name_map:
        return eve_servers_name_map[server_name]

    abort(400)


def get_server_status(server):
    """Gets the server status for a specified server."""
    try:
        url = eve_servers[server]
        r = requests.get(url)
    
        if r.status_code == requests.codes.ok:
            json = r.json()
    
            status = json['serviceStatus']['eve']
            player_count = json['userCounts']['eve']
            version = json['serverVersion']
    
            if status == 'online':
                status = status.capitalize()
    
            elif status == 'vip':
                status = status.upper()
    
            return {
                'title': server.capitalize(),
                'value': '*{}:* {:,d}\n*Version:* {}'.format(status, player_count, version),
                'short': True,
            }
            
    except requests.exceptions.ConnectionError:
        return {
            'title': server.capitalize(),
            'value': '*Offline*',
            'short': True,
        }


def get_all_server_status():
    """Gets the status of all servers."""
    statuses = [get_server_status(server_name) for server_name in eve_servers.keys()]
    return sorted(statuses, key=lambda k: k['title']) 
