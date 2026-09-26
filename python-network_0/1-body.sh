#!/bin/bash
# This script displays the body only when the server returns an HTTP 200 status.
curl -s -o /tmp/body -w '%{http_code}' "$1" | grep -q '^200$' && cat /tmp/body
