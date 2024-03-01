#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response
"""

import sys
import requests

url = sys.argv[1]
re = requests.get(url)

if __name__ == "__main__":
    if re.status_code != requests.code.ok:
        print('Error code: {}'.format(response.status_code))
    else:
        print(re.text)
