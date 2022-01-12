import os
import json
from json.decoder import JSONDecodeError
from argparse import Namespace
from typing import Dict, Any, List
from mvgcli.departures_request import DeparturesRequest
from mvgcli.next_departures import print_next_departures
from mvgcli.config import CONFIG_DIRECTORY, use_config_dir


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
    use_config_dir()
    with open(FAVORITES_FILE_PATH, 'w') as f:
        json.dump(favorites, f)


def print_favorites():
    favorites = _read_favorites()
    
    for (i, favorite) in enumerate(favorites):
        request = DeparturesRequest(data_dict=favorite)
        print_next_departures(request)
        if i < len(favorites) - 1:
            print('\n')


def list_favorites(_: Namespace):
    favorites = _read_favorites()
    if len(favorites) == 0:
        print('You currently do not have any favorites. Add one using `mvg favorites add`.')
    
    max_num_width = len(str(len(favorites) - 1))
    for (i, favorite) in enumerate(favorites):
        request = DeparturesRequest(data_dict=favorite)
        padding = ' ' * (max_num_width - len(str(i)))
        print(f'{padding}{i}: {request.get_description()}')


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


def remove_favorite(args: Namespace):
    index = args.index
    favorites = _read_favorites()

    if len(favorites) == 0:
        print('You currently do not have any favorites.')
        return

    if index >= len(favorites) or index < 0:
        print(f'Index out of bounds. Please specify an index between 0 and {len(favorites) - 1}.')
        return

    favorites.pop(index)
    _write_favorites(favorites)

    print(f'Removed setting from your favorites. You now have {len(favorites)} favorite(s) in total.')