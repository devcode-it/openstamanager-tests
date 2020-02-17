from argparse import ArgumentParser
import os
import glob
import string
import random
import json
import re

def random_string(size=32, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits) -> str:
    ''' Restituisce una stringa di caratteri causali.'''
    return ''.join(random.choice(chars) for _ in range(size))

def get_cache_directory() -> str:
    ''' Restituisce il percorso della cartella di cache degli scripts.'''

    directory = __file__
    directory = os.path.dirname(directory)

    cache_directory = os.path.join(os.path.dirname(directory), 'cache')
    if not os.path.exists(cache_directory):
        os.mkdir(cache_directory)

    return cache_directory

def get_config() -> dict:
    ''' Restituisce la configurazione prevista dal file config.json.'''

    directory = get_cache_directory()
    directory = os.path.dirname(directory)

    filename = directory + '/config.json'

    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

            return data
    else:
        return dict()

def update_config(config) -> None:
    ''' Restituisce la configurazione prevista dal file config.json.'''

    directory = get_cache_directory()
    directory = os.path.dirname(directory)

    filename = directory + '/config.json'

    with open(filename, 'w+') as json_file:
        json.dump(config, json_file, indent=4, sort_keys=True)

def get_args() -> dict:
    parser = ArgumentParser()

    parser.add_argument("-a", "--action", dest="action", help="Imposta l'azione da eseguire", metavar="ACTION")

    args = parser.parse_args()

    return args

def list_files(path: str) -> list:
    files = glob.glob(path + '/**/*', recursive=True)
    hidden_files = glob.glob(path + '/**/.*', recursive=True)

    return files + hidden_files
