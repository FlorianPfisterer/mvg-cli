from argparse import Namespace
from datetime import datetime
from mvg_api import Station


def _get_prefix(departure) -> str:
    return f"{departure['label']} {departure['destination']}"


def get_next_departures(args: Namespace):
    station_name = args.start_station
    station = Station(station_name)

    if station is None:
        print(f'Could not find station for query {station_name}.')
        return

    print(f'Upcoming departures from {station.name}\n')

    departures = station.get_departures(timeoffset=args.offset)
    dest_station = args.dest_station if args.dest_station is not None else None

    longest_prefix = ''
    valid_departures = []
    i = 0
    while len(valid_departures) <= args.limit and i < len(departures):
        departure = departures[i]
        i += 1

        if dest_station is not None and dest_station not in departure['destination']:
            continue
 
        prefix = _get_prefix(departure)
        longest_prefix = prefix if len(prefix) > len(longest_prefix) else longest_prefix
        valid_departures.append(departure)

    padding_length = len(longest_prefix) + 5
    valid_departures = sorted(valid_departures, key=lambda d: d['departureTimeMinutes'])
    for departure in valid_departures: 
        time = datetime.fromtimestamp(int(departure['departureTime']) / 1000).strftime('%H:%M')

        delay = departure['delay'] if 'delay' in departure else 0
        delay = f'+{delay}' if delay >= 0 else f'{delay}'

        prefix = _get_prefix(departure)
        padding = ' ' * (padding_length - len(prefix))

        time_mins = departure['departureTimeMinutes']
        relative_description = f'in {time_mins} min' if time_mins >= 0 else 'now'

        print(f"{prefix}{padding}{time} {delay} ({relative_description})")