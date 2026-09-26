#!/usr/bin/python3
"""Fetches the intranet status and displays information about its body."""
import urllib.request


def fetch_status():
    """Fetches the intranet status and displays its response body."""
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))


if __name__ == "__main__":
    fetch_status()
