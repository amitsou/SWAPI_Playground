import os
import sys
import json
import datetime
import argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.utils as utils


def parse_args():
    """ Parse the command line arguments
    Returns:
        argparse.Namespace: The parsed arguments
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='commands', dest='command', required=True)

    search_parser = subparsers.add_parser('search', help='Search for a Star Wars character by name')
    search_parser.add_argument('name', help='The name of the character to search for')
    search_parser.add_argument('--world', action='store_true', help='Provide the correlation between an earth day and an earth year for the character\'s world')

    cache_parser = subparsers.add_parser('cache', help='Cache-related commands')
    cache_parser.add_argument('--clean', action='store_true', help='Clean the cache')
    return parser.parse_args()


def main():
    args = parse_args()
    cache_file = 'cache.json'
    cache_file_path = os.path.join(os.getcwd(),cache_file)

    if args.command == 'search':
        character_name_url = f'https://swapi.dev/api/people/?search={args.name}'

        if not utils.is_file(cache_file_path):
            open(cache_file_path, 'w').close()

        cached_data = utils.load_cache(cache_file_path)

        if args.name in cached_data:
            print('data in cache')
            response = cached_data[args.name]['response']
            timestamp = cached_data[args.name]['timestamp']
        else:
            print('data not in cache')
            response = utils.swapi_get_request(character_name_url)
            response = response.json()
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")

            cached_data[args.name] = {"response": response, "timestamp": timestamp}
            utils.save_in_cache(cache_file_path, cached_data)

        utils.get_character_info(response, timestamp, args.name, args.world)

    elif args.command == 'cache':
        utils.clean_cache(cache_file_path)


if __name__ == "__main__":
    main()