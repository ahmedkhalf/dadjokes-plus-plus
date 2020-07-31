__version__ = "1.0.0"

import requests


URL = "https://github.com/ahmedkhalf/dadjokes-plus-plus"
USER_AGENT = f"dadjokes-plus-plus/v{__version__} ({URL})"
HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}


def joke():
    """Fetches a random dad joke."""
    r = requests.get("https://icanhazdadjoke.com/", headers=HEADERS)
    return r.json()["joke"]
