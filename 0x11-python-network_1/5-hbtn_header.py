#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    re = requests.get(url)
    print(re.headers.get('X-Request-Id'))
