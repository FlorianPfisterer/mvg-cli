import argparse
from mvgcli.next_departures import get_next_departures

parser = argparse.ArgumentParser(prog='mvg', description='Access MVG data from your command line.')
subparsers = parser.add_subparsers(title='sub-commands')

dep_parser = subparsers.add_parser('dep')
dep_parser.add_argument('--from', '-f', metavar='f', type=str, nargs='?', required=True, dest='start_station',
                        help='the starting point from which you want to see the next rides')
dep_parser.add_argument('--to', '-to', metavar='t', type=str, nargs='?', required=False, dest='dest_station',
                        help='filter departures by destination station')
dep_parser.add_argument('--offset', '-o', metavar='o', type=int, nargs='?', required=False, dest='offset', default=0,
                        help='the number of minutes from now at which to look for rides')
dep_parser.add_argument('--limit', '-l', metavar='l', type=int, nargs='?', required=False, dest='limit', default=5,
                        help='limit the number of results (upto approximately 25 can be returned)')
dep_parser.set_defaults(func=get_next_departures)

def main():
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()