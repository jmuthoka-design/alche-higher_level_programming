#!/bin/bash
# This script displays the HTTP methods accepted by the server at the given URL.
curl -s -X OPTIONS -i "$1" | grep -i '^Allow:' | cut -d' ' -f2-
