#!/bin/bash
# Sends a GET request to a URL with a header variable with value 98
curl -sH "X-School-User-Id: 98" "$1"
