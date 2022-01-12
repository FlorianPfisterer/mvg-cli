import argparse
from mvgcli.next_departures import get_next_departures

parser = argparse.ArgumentParser(prog='mvg', description='Access live MVG data from your command line.')
parser.add_argument('--from', '-f', metavar='f', type=str, nargs='?', required=True, dest='start_station',
                    help='the starting point from which you want to see the next rides')
parser.add_argument('--to', '-to', metavar='t', type=str, nargs='?', required=False, dest='dest_station',
                    help='filter departures by final destination station')
parser.add_argument('--offset', '-o', metavar='o', type=int, nargs='?', required=False, dest='offset', default=0,
                    help='the number of minutes from now at which to look for rides, 0 by default')
parser.add_argument('--limit', '-l', metavar='l', type=int, nargs='?', required=False, dest='limit', default=5,
                    help='limit the number of results (upto approximately 25 can be returned), 5 by default')
parser.set_defaults(func=get_next_departures)


def main():
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()