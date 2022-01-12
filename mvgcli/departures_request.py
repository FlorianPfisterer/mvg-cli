from typing import Optional, Any, Dict, List
from argparse import Namespace
from mvg_api import Station


class DeparturesRequest:
    start_station_name: str
    dest_station_filter: Optional[str]
    offset: int
    limit: int

    station: Optional[Station] = None

    def __init__(self, args: Optional[Namespace] = None, data_dict: Optional[Dict[str, Any]] = None):
        if args is not None:
            self.start_station_name = args.start_station
            self.dest_station_filter = args.dest_station
            self.offset = args.offset if args.offset is not None else 0
            self.limit = args.limit if args.limit is not None else 5
        elif data_dict is not None:
            self.start_station_name = data_dict['start']
            self.dest_station_filter = data_dict['dest'] if 'dest' in data_dict else None
            self.offset = data_dict['offset'] if 'offset' in data_dict else 0
            self.limit = data_dict['limit'] if 'limit' in data_dict else 5
        else:
            raise ValueError('you need to either supply args or a data_dict to the initializer')

    def get_station(self) -> Optional[Station]:
        if self.station is not None:
            return self.station

        try:
            self.station = Station(self.start_station_name)
            self.start_station_name = self.station.name
            return self.station
        except NameError:
            return None

    def get_departures(self) -> List[Dict[str, Any]]:
        station = self.get_station()
        departures = station.get_departures(timeoffset=self.offset)

        valid_departures = []
        i = 0
        while len(valid_departures) <= self.limit and i < len(departures):
            departure = departures[i]
            i += 1

            if self.dest_station_filter is not None and self.dest_station_filter not in departure['destination']:
                continue

            valid_departures.append(departure)

        return valid_departures

    def get_description(self) -> str:
        station = self.get_station()
        to_filter = f' to {self.dest_station_filter}' if self.dest_station_filter is not None else ''
        offset_filter = f' in {self.offset} min' if self.offset > 0 else ''
        return f'from {station.name}{to_filter}{offset_filter}'

    def get_dict(self) -> Dict[str, Any]:
        return {
            'start': self.start_station_name,
            'dest': self.dest_station_filter,
            'offset': self.offset,
            'limit': self.limit
        }