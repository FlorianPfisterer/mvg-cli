from argparse import Namespace
from datetime import datetime

from mvgcli.departures_request import DeparturesRequest


def _get_prefix(departure) -> str:
    return f"{departure['label']} {departure['destination']}"


def get_next_departures(args: Namespace):
    print_next_departures(DeparturesRequest(args=args))


def print_next_departures(request: DeparturesRequest):
    station = request.get_station()
    if station is None:
        print(f'Could not find station for query {request.start_station_name}.')
        return

    to_filter = f' to {request.dest_station_filter}' if request.dest_station_filter is not None else ''
    offset_filter = f' in {request.offset} min' if request.offset > 0 else ''
    print(f'Upcoming departures from {station.name}{to_filter}{offset_filter}\n')

    departures = request.get_departures()
    longest_prefix = ''
    for departure in departures:
        prefix = _get_prefix(departure)
        longest_prefix = prefix if len(prefix) > len(longest_prefix) else longest_prefix

    padding_length = len(longest_prefix) + 5
    departures = sorted(departures, key=lambda d: d['departureTimeMinutes'])

    for departure in departures: 
        time = datetime.fromtimestamp(int(departure['departureTime']) / 1000).strftime('%H:%M')

        delay = departure['delay'] if 'delay' in departure else 0
        delay = f'+{delay}' if delay >= 0 else f'{delay}'

        prefix = _get_prefix(departure)
        padding = ' ' * (padding_length - len(prefix))

        time_mins = departure['departureTimeMinutes']
        relative_description = f'in {time_mins} min' if time_mins >= 0 else 'now'

        print(f"{prefix}{padding}{time} {delay} ({relative_description})")