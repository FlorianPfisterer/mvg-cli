from argparse import Namespace
from datetime import datetime
from mvg_api import Station


def get_next_departures(args: Namespace):
    station_name = args.start_station
    station = Station(station_name)

    if station is None:
        print(f'Could not find station for query {station_name}.')
        return

    departures = station.get_departures(timeoffset=args.offset)

    print(f'Next departures from {station.name}:\n')
    dest_station = args.dest_station if args.dest_station is not None else None
    longest_name = ''

    valid_departures = []
    i = 0
    while len(valid_departures) <= args.limit and i < len(departures):
        departure = departures[i]
        i += 1

        if dest_station is not None and dest_station not in departure['destination']:
            continue
 
        longest_name = departure['destination'] if len(departure['destination']) > len(longest_name) else longest_name
        valid_departures.append(departure)

    padding_length = len(longest_name) + 5
    valid_departures = sorted(valid_departures, key=lambda d: d['departureTimeMinutes'])
    for departure in valid_departures: 
        time = datetime.fromtimestamp(int(departure['departureTime']) / 1000).strftime('%H:%M')
        delay = departure['delay'] if 'delay' in departure else 0
        padding = ' ' * (padding_length - len(departure['destination']))

        time_mins = departure['departureTimeMinutes']
        relative_description = f'in {time_mins} min' if time_mins >= 0 else 'now'
        print(f"{departure['label']} to {departure['destination']}{padding}{time} +{delay} ({relative_description})")