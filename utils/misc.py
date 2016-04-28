

def get_character_links(character_name, character_id):
    gate_url = 'https://gate.eveonline.com/Profile/{}/'.format(character_name)
    search_url = 'http://eve-search.com/search/author/{}/'.format(character_name)
    board_url = 'http://eveboard.com/pilot/{}/'.format(character_name)
    who_url = 'http://evewho.com/pilot/{}/'.format(character_name)
    hunt_url = 'http://eve-hunt.net/hunt/{}/'.format(character_name)
    zkb_url = 'https://zkillboard.com/character/{}/'.format(character_id)

    links = [
        '<{}|EVE Gate>'.format(gate_url),
        '<{}|EVE Hunt>'.format(hunt_url),
        '<{}|EVE Search>'.format(search_url),
        '<{}|EVE Who>'.format(who_url),
        '<{}|eveboard>'.format(board_url),
        '<{}|zKillboard>'.format(zkb_url),
    ]
    
    return ' // '.join(links)
