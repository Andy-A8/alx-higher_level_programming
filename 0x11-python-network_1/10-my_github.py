#!/usr/bin/bash
"""
    Takes my GitHub credentials (username and password) and uses
    the GitHub API to display your id:
    You must use Basic Authentication with a personal access token as password
    to access to your information (only read:user permission is needed)
    The first argument will be your username
    The second argument will be your password
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'

    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    r = req.json()
    print(r.get('id'))
