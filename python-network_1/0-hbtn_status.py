#!/usr/bin/python3
"""This module fetches and displays the status of the ALU intranet server."""
import urllib.request


with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
