#!/bin/bash
# Sends a JSON POST request to a URL passed with contents of a file
curl -s POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
