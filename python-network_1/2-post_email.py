#!/usr/bin/python3
"""This module sends an email as a POST parameter to a specified URL."""
import sys
import urllib.request
import urllib.parse


def post_email():
    """Sends an email to the given URL and displays the response body."""
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    request = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    post_email()
