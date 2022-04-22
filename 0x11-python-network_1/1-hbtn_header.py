#!/usr/bin/python3
""" Get value from header """

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io') as response:
    print(response.getheader('X-Request-Id'))
