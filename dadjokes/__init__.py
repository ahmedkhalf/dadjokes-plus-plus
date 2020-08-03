__version__ = "1.2"

import requests
import os.path
import time
import random


URL = "https://github.com/ahmedkhalf/dadjokes-plus-plus"
USER_AGENT = f"dadjokes-plus-plus/v{__version__} ({URL})"
HEADERS = {"User-Agent": USER_AGENT, "Accept": "application/json"}


def _request(query={}, search=False):
    if search:
        url = "https://icanhazdadjoke.com/search"
        return requests.get(url, params=query, headers=HEADERS)
    return requests.get("https://icanhazdadjoke.com/", headers=HEADERS)


def save_jokes(path):
    if os.path.exists(path):
        print("File exists at: ", path)
        prompt = input("Would you like to overwrite the file [Yn]? ")
        if prompt.lower() == "n":
            return False
    with open(path, "w", encoding="utf-8") as f:
        first = True
        page = 1
        pages = None
        while pages is None or page <= pages:
            r = _request(search=True, query={"page": str(page), "limit": "30"})
            result = r.json()

            if first:
                first = False
                pages = int(result["total_pages"])

            for leaf in result["results"]:
                joke = str(leaf["joke"])
                joke = joke.splitlines()
                joke = list(filter(bool, joke))
                f.write("_NEWLINECHAR_".join(joke) + "\n")

            print(f"[{page}/{pages}]", end="\r", flush=True)
            page += 1
            # Wait at least one second between requests
            time.sleep(1)


def _random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line.replace("_NEWLINECHAR_", "\n")


def joke(file=None):
    """Fetches a random dad joke."""
    if file is not None:
        with open(file, "r", encoding="utf-8") as f:
            return _random_line(f)
    else:
        r = _request()
        return r.json()["joke"]
