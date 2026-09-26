#!/usr/bin/python3
"""Fetches a URL and displays information about its response body."""
import urllib.request


def fetch_status(url):
    """Fetches the given URL and displays its response body information."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))


if __name__ == "__main__":
    fetch_status("https://alu-intranet.hbtn.io/status")
