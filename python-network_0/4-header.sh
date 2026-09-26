#!/bin/bash
# This script sends a GET request with the required user ID header.
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
