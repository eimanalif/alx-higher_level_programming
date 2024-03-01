#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    bytes_content = response.read()
    content = bytes_content.decode('utf-8')


if __name__ == "__main__":
    print_string = '''Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}'''.format(type(bytes_content), bytes_content, content)
    print(print_string)
