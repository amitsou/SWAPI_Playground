import os
import re
import sys
import json
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout


def get_character_info(swapi_response:dict, timestamp:str, search_term:str, homeworld:str=None):
    """
        Search for a Star Wars character by name using the SWAPI api and
        print out information about the character (if any).
        In case the homeworld argument is specified, print out information
        about the character's homeworld (if any)

    Args:
        swapi_response (dict): The response from the SWAPI API.
        timestamp (str): The timestamp for the cached response.
        search_term (str): The search term to match against the character name.
        homeworld (str, optional): The name of the character's homeworld to display
                               information for. Defaults to None.
    """

    if swapi_response['results'] != [] and re.search(search_term, swapi_response['results'][0]['name'], re.IGNORECASE):
        try:
                character_info = swapi_response['results'][0]
                print(f"Name: {character_info['name']}")
                print(f"Height: {character_info['height']}")
                print(f"Mass: {character_info['mass']}")
                print(f"Birth Year: {character_info['birth_year']}")

                if homeworld:
                    homeworld_url = character_info['homeworld']
                    response = swapi_get_request(homeworld_url)
                    homeworld_info = response.json()

                    print('\n\n\nHomeWorld\n----------------')
                    print(f"Name: {homeworld_info['name']}")
                    print(f"Population: {homeworld_info['population']}\n\n")

                    homeworld_year = int(homeworld_info['orbital_period']) / 365
                    homeworld_day = int(homeworld_info['rotation_period']) / 24
                    print(f"On {homeworld_info['name']}, 1 year on Earth is {homeworld_year:.2f} years and 1 day is {homeworld_day:.2f} Earth days.")
                print(f'\n\ncached: {timestamp}')

        except (IndexError,KeyError,ValueError) as e:
            print(f'Error: {e}')
    else:
        print('The force is not strong within you')


def swapi_get_request(url:str):
    """
        Send an HTTP GET request to the SWAPI api using
        the specified URL and return the response object.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        requests.Response: The response object from the GET request.

    Raises:
        ValueError: If there is an error sending the GET request or if the response status code is not 200 OK.
    """


    try:
        response = requests.get(url)
        response.raise_for_status()
        return response

    except (HTTPError,ConnectionError,Timeout) as e:
        raise ValueError(f'Error getting SWAPI data: {e}')


def clean_cache(cache_file:str):
    """ Removes the cache file if it exists

    Args:
        cache_file (str): The absolute path to the cache file
    """
    if os.path.isfile(path=cache_file):
        os.remove(cache_file)
        print('removed cache')

def save_in_cache(cache_file:str, cache:dict):
    """ Saves the cache dictionary to the cache file

    Args:
        cache_file (str): The absolute path to the cache file
        cache (dict): The cache dictionary to save to the cache file
    """
    with open(cache_file, 'w') as f:
        json.dump(cache, f)


def load_cache(cache_file:str):
    """ Loads the cache file into a dictionary

    Args:
        cache_file (str): The absolute path to the cache file

    Returns:
        dict_: The cache file as a dictionary
    """
    with open(cache_file) as f:
        json_str = f.read()

    try:
        return json.loads(json_str)
    except json.decoder.JSONDecodeError:
        return {}


def is_file(filename: str) -> bool:
    """ Checks if the specified file exists

    Args:
        filename (str): The file to check

    Returns:
        bool: True if the file exists, False if the file does not exist
    """
    return os.path.isfile(path=filename)