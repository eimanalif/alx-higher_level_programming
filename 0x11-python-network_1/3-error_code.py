#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.error

url = sys.argv[1]

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
