#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response
"""

if __name__ == "__main__":

    import sys
    import requests

    url = sys.argv[1]
    re = requests.get(url)
    if re.status_code >= 400:
        print("Error code: {}".format(re.status_code))
    else:
        print(re.text)
