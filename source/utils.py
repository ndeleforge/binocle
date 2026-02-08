import json
import sys
from tabulate import tabulate
from __init__ import PATH

def show_version(name, version) :
    """
    Display the name and the version
    """

    print(f"{name} v{version}")


def show_engines(engines) :
    """
    Display engines in alphabetical order
    """

    sorted_engines = sorted(engines, key=lambda e: e['name'])
    table_data = [(e['keyword'], e['name']) for e in sorted_engines]
    print(tabulate(table_data, headers=["Keyword", "Name"], tablefmt="pipe"))


def is_virtual_env():
    """
    Check if Binocle is running into a virtual environment
    """

    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)


def load_json(name_file):
    """
    Load a JSON file and returns the values
    """

    try:
        with open(f"{PATH}/config/{name_file}.json", 'r', encoding='utf-8') as file:
            file_content = json.load(file)
            return file_content

    except FileNotFoundError:
        print(f"An error occurred: {name_file} file does not exist.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"An error occurred: {name_file} is not a valid JSON.")
        sys.exit(1)


def check_uniqueness(engines):
    """
    Check if specified fields in the JSON config file are unique. If not, returns an error
    """

    json_fields = ['name', 'keyword', 'url']

    def check_field(field):
        all_fields = [engine[field] for engine in engines]
        unique_fields = set(all_fields)
        if len(all_fields) != len(unique_fields):
            print(f"An error occured: each {field} in the engine list must be unique.")
            sys.exit(1)

    for field in json_fields:
        check_field(field)


def check_config(config, engines):
    """
    Check if config file is not empty or correctly filled
    """

    required_fields = {
        "default_engine": str,
        "warning_venv": bool,
    }

    for key, expected_type in required_fields.items():
        if key not in config:
            print(f"An error occured: {key} does not exist in the config file while it is a mandatory setting.")
            sys.exit(1)

        if not isinstance(config[key], expected_type):
            print(f"An error occured: {key} values does not respect its type, please refer to the documentation.")
            sys.exit(1)

        if expected_type == str and not config[key].strip():
            print(f"An error occured: {key} does not have any values while it is a mandatory setting.")
            sys.exit(1)

    available_names = [engine["name"] for engine in engines]
    if config["default_engine"] not in available_names:
        print(f"An error occured: '{config['default_engine']}' is not a valid engine name.")
        sys.exit(1)
