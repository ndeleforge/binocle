#!/usr/bin/env python3

"""
Look everything, everywhere.
Usage: binocle "my research"
"""

import argparse
import sys
import webbrowser
from tabulate import tabulate
from __init__ import *
from utils import *

# Arguments parser

parser = argparse.ArgumentParser(
    prog=NAME,
    usage="%(prog)s [-h] [-v] [-l] engine query",
    description="Look for everything, everywhere"
)
parser.add_argument( "-v", "--version", action="store_true", help="show version")
parser.add_argument("-l", "--list", action="store_true", help="show engines list and exit")
parser.add_argument("engine", nargs="?", type=str, help="search engine (ex : d for duckduckgo)")
parser.add_argument("query", nargs="?", type=str, help="search query (ex : \"my super research\")")
NBARGS = len(sys.argv) - 1

# Load configuration

ENGINES = load_json("engines")
check_uniqueness(ENGINES)
CONFIG = load_json("config")
check_config(CONFIG, ENGINES)

# Search functions

def search_engine() :
    """ 
    Search for the correct engine
    """

    chosen_engine = parser.parse_args().engine
    query = parser.parse_args().query

    for engine in ENGINES :
        if engine["keyword"] == chosen_engine :
            launch_search(engine, query)
            return

    print(
        f"{NAME}: '{chosen_engine}' is not a configured engine. "
        "Please use the argument '-l' to look at all the available engines."
    )


def  launch_search(engine, query) :
    """
    Launch a search on the specified engine with the given query
    """

    query_formatted = engine['url'] + query.replace(' ', '%20')
    table_data = [
        ["Engine", engine['name']],
        ["Query", query],
        ["Formatted query", query_formatted]
    ]

    show_version(NAME, VERSION)
    print(tabulate(table_data, tablefmt="plain"))
    webbrowser.open(query_formatted, new=2)


def binocle():
    """
    Main function of the Binocle search application
    """

    if CONFIG["warning_venv"] and not is_virtual_env():
        print("warning : binocle is currently not running into a virtual environment.\n")

    # No argument, display help
    if NBARGS == 0:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # 2nd case
    # Optionnal argument or default engine
    elif NBARGS == 1:
        arg = sys.argv[1]

        # Show help
        if arg in ('-h', '--help'):
            parser.print_help(sys.stderr)
            sys.exit(1)

        # Show version
        if arg in ('-v', '--version'):
            show_version(NAME, VERSION)
            sys.exit(1)

        # Show engine list
        if arg in ('-l', '--list'):
            show_engines(ENGINES)
            sys.exit(1)

        # Default engine
        else:
            default_engine = CONFIG["default_engine"]
            engine = next((e for e in ENGINES if e["name"] == default_engine), None)
            query = arg
            launch_search(engine, query)

    # 3rd case
    # Normal case with two arguments : engine and query
    else:
        search_engine()


if __name__ == "__main__":
    binocle()
