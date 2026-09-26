#!/usr/bin/python3
"""This module retrieves and displays a response header from a given URL."""
import sys
import urllib.request


def display_request_id():
    """Fetches the URL and displays its X-Request-Id response header."""
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    display_request_id()
