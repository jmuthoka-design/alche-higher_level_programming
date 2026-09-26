#!/bin/bash
# This script sends a GET request with the required Holberton School user ID header.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
