import argparse
from mvgcli.next_departures import get_next_departures
from mvgcli.favorites import add_favorite, print_favorites, list_favorites, remove_favorite
from mvgcli.defaults import update_defaults, MIN_TO_STATION

parser = argparse.ArgumentParser(prog='mvg', description='Access live MVG data from your command line.')
subparsers = parser.add_subparsers(title='sub-commands', description='available subcommands for settings')

parser.add_argument('--from', '-f', metavar='f', type=str, nargs='?', required=False, dest='start_station',
                    help='the starting point from which you want to see the next rides')
parser.add_argument('--to', '-to', metavar='t', type=str, nargs='?', required=False, dest='dest_station', default=None,
                    help='filter departures by final destination station')
parser.add_argument('--offset', '-o', metavar='o', type=int, nargs='?', required=False, dest='offset', default=0,
                    help='the number of minutes from now at which to look for rides, 0 by default')
parser.add_argument('--limit', '-l', metavar='l', type=int, nargs='?', required=False, dest='limit', default=5,
                    help='limit the number of results (upto approximately 25 can be returned), 5 by default')

favorite_parser = subparsers.add_parser('favorites')
favorite_subparsers = favorite_parser.add_subparsers(title='favorite management commands')
add_favorite_parser = favorite_subparsers.add_parser('add')
add_favorite_parser.add_argument('--from', '-f', metavar='f', type=str, nargs='?', required=True, dest='start_station',
                                 help='the starting point from which the favorite should start')
add_favorite_parser.add_argument('--to', '-to', metavar='t', type=str, nargs='?', required=False, dest='dest_station', default=None,
                                 help='filter departures by final destination station in the favorite')
add_favorite_parser.add_argument('--offset', '-o', metavar='o', type=int, nargs='?', required=False, dest='offset', default=0,
                                 help='the number of minutes from now at which to look for rides each time the favorite is requested, 0 by default')
add_favorite_parser.add_argument('--limit', '-l', metavar='l', type=int, nargs='?', required=False, dest='limit', default=5,
                                 help='limit the number of results in the favorite (upto approximately 25 can be returned), 5 by default')
add_favorite_parser.set_defaults(func=add_favorite)

list_favorite_parser = favorite_subparsers.add_parser('list')
list_favorite_parser.set_defaults(func=list_favorites)

remove_favorite_parser = favorite_subparsers.add_parser('remove')
remove_favorite_parser.add_argument('--index', '-i', metavar='i', type=int, nargs='?', required=True, dest='index',
                                    help='the index of the favorite setting you want to remove')
remove_favorite_parser.set_defaults(func=remove_favorite)

defaults_parser = subparsers.add_parser('defaults')
defaults_parser.add_argument('key', metavar='k', type=str, nargs='?', choices=[MIN_TO_STATION],
                            help='which field of the default settings you want to edit')
defaults_parser.add_argument('value', metavar='v', type=str, nargs='?',
                            help='the value to which you want to set the given field')
defaults_parser.set_defaults(func=update_defaults)


def main():
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    elif hasattr(args, 'start_station') and args.start_station is not None:
        get_next_departures(args)
    else:
        print_favorites()


if __name__ == '__main__':
    main()