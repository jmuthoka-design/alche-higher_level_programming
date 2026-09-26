#!/usr/bin/python3
"""This module fetches and displays the status of the ALU intranet server."""
import requests


def fetch_status():
    """Fetches the intranet status and displays information about its body."""
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)


if __name__ == "__main__":
    fetch_status()
    
