import os
import json
from argparse import Namespace
from json.decoder import JSONDecodeError
from typing import Any, Dict
from mvgcli.config import CONFIG_DIRECTORY, use_config_dir

MIN_TO_STATION = 'min-to-station'
DEFAULTS_FILE_PATH = os.path.join(CONFIG_DIRECTORY, 'defaults.json')


def get_defaults() -> Dict[str, Any]:
    if not os.path.isfile(DEFAULTS_FILE_PATH):
        return {}

    with open(DEFAULTS_FILE_PATH, 'r') as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return {}


def _write_defaults(defaults: Dict[str, Any]):
    use_config_dir()
    with open(DEFAULTS_FILE_PATH, 'w') as f:
        json.dump(defaults, f)


def update_defaults(args: Namespace):
    key = args.key
    value = args.value

    if key is None or value is None:
        print('Please specify a key and a value.')
        return

    try:
        value = int(value)
    except ValueError:
        pass

    set_defaults(key, value)
    print(f'Successfully set defaults.{key} = {value}.')


def set_defaults(key: str, value: Any):
    defaults = get_defaults()
    defaults[key] = value
    _write_defaults(defaults)
