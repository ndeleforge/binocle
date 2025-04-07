import sys
import requests

def show_version(name, version) :
    """ Display the name and the version """

    print(f"{name} v{version}")
    check_update(version)

def show_engines(engines) :
    """ Display engines in alphabetical order """

    from tabulate import tabulate

    sorted_engines = sorted(engines, key=lambda e: e['name'])
    table_data = [(e['keyword'], e['name']) for e in sorted_engines]
    print(tabulate(table_data, headers=["Keyword", "Name"], tablefmt="pipe"))

def is_virtual_env():
    """ Check if Binocle is running into a virtual environment """

    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

def check_update(version):
    """
    Compare current version to the latest GitLab release.
    """
    api_url = f"https://api.github.com/repos/ndeleforge/binocle/releases/latest"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        latest = data["tag_name"]

        if (latest > version):
            print(f"An update is available ! Please check on Github to get the new version {latest}.")
        else:
            print(f"The current version {version} is the latest available.")

    except requests.RequestException as e:
        print(f"An error occured when checking if an update is available.")