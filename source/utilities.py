from tabulate import tabulate
from __init__ import NAME, VERSION
from binocle import ENGINES
import sys

def show_version() :
    """
    Display the name and the version
    """

    print(f"{NAME} v{VERSION}")

def show_engines() :
    """
    Display engines in alphabetical order
    """

    sorted_engines = sorted(ENGINES, key=lambda e: e['name'])
    table_data = [(e['keyword'], e['name']) for e in sorted_engines]
    print(tabulate(table_data, headers=["Keyword", "Name"], tablefmt="pipe"))

def is_virtual_env():
    """
    Check if Binocle is running into a virtual environment
    """
    
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)