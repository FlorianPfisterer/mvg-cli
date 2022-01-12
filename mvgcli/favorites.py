from json.decoder import JSONDecodeError
import os
import json
from argparse import Namespace
from typing import Dict, Any, List
from mvgcli.departures_request import DeparturesRequest
from mvgcli.next_departures import print_next_departures

CONFIG_DIRECTORY = os.path.join(os.path.expanduser('~'), '.mvgcli')
FAVORITES_FILE_PATH = os.path.join(CONFIG_DIRECTORY, 'favorites.json')


def _read_favorites() -> List[Dict[str, Any]]:
    if not os.path.isfile(FAVORITES_FILE_PATH):
        return []

    with open(FAVORITES_FILE_PATH, 'r') as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []


def _write_favorites(favorites: List[Dict[str, Any]]):
    if not os.path.isdir(CONFIG_DIRECTORY):
        os.mkdir(CONFIG_DIRECTORY)

    with open(FAVORITES_FILE_PATH, 'w') as f:
        json.dump(favorites, f)


def print_favorites():
    favorites = _read_favorites()
    
    for (i, favorite) in enumerate(favorites):
        request = DeparturesRequest(data_dict=favorite)
        print_next_departures(request)
        if i < len(favorites) - 1:
            print('\n')


def add_favorite(args: Namespace):
    request = DeparturesRequest(args=args)
    station = request.get_station()

    if station is None:
        print(f'Could not find station for query {request.start_station_name}.')
        return

    # store the favorite
    data_dict = request.get_dict()
    favorites = _read_favorites()
    favorites.append(data_dict)

    _write_favorites(favorites)
    print(f'Added setting to your favorites. You now have {len(favorites)} favorite(s) in total.')