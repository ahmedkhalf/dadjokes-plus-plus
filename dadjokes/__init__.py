__version__ = "1.0.0"

import requests


USER_AGENT = f"dadjokes-plus-plus/v{__version__} (https://github.com/ahmedkhalf/dadjokes-plus-plus)"
HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}


def joke():
    """Fetches a random dad joke."""
    r = requests.get("https://icanhazdadjoke.com/", headers=HEADERS)
    return r.json()["joke"]

