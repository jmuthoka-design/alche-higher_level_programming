#!/bin/bash
# Sends a GET request to the given URL and displays the body only if the status code is 200
curl -s -w '\n%{http_code}' "$1" | awk 'NR==1{b=$0;next}{c=$0}END{if(c==200)print b}'
