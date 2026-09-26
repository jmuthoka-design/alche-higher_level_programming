#!/usr/bin/python3
"""This module fetches a URL and displays information about its response."""
import sys
import requests


def fetch_status():
    """Fetches the requested URL and displays its response body."""
    url = sys.argv[1] if len(sys.argv) > 1 else "https://intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    fetch_status()
    
