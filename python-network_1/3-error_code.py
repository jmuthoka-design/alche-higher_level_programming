#!/usr/bin/python3
"""This module fetches a URL and handles HTTP errors from the response."""
import sys
import urllib.request
import urllib.error


def fetch_url():
    """Fetches the given URL and displays its response or HTTP error code."""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)


if __name__ == "__main__":
    fetch_url()
