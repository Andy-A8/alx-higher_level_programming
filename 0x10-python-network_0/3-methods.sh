#!/bin/bash
# Displays all HTTP methods the server of a URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
