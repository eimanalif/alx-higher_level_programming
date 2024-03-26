#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

url = "https://alx-intranet.hbtn.io/status"
res = requests.get(url)
content = res.text


if __name__ == "__main__":
    print_string = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
    print(print_string)
