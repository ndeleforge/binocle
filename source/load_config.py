import json
import sys
from __init__ import PATH

def load_json(name_file):
    """ Load a JSON file and returns the values """
    
    try:
        with open(f"{PATH}/config/{name_file}.json", 'r', encoding='utf-8') as file:
            FILE = json.load(file)
            return FILE.get(name_file, [])
    except FileNotFoundError:
        print(f"An error occurred: {name_file} file does not exist.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"An error occurred: {name_file} is not a valid JSON.")
        sys.exit(1)

def check_uniqueness(engines):
    """ Check if specified fields in the JSON config file are unique. If not, returns an error """

    json_fields = ['name', 'keyword', 'url']

    def check_field(field):
        all_fields = [engine[field] for engine in engines]
        unique_fields = set(all_fields)
        if len(all_fields) != len(unique_fields):
            print(f"Error! Each {field} in the engine list must be unique.")
            sys.exit(1)

    for field in json_fields:
        check_field(field)
