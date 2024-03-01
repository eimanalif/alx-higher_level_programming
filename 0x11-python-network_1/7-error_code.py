#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response
"""

if __name__ == "__main__":

    import sys
    import requests

    url = sys.argv[1]
    reponse = requests.get(url)
    if response.status_code != requests.code.ok:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
