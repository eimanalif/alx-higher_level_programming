#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""
import sys
import requests

url = sys.argv[1]
re = requests.get(url)

if __name__ == "__main__":
    print(re.headers.get('X-Request-Id'))
