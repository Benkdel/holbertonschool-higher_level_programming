#!/usr/bin/python3
""" fetch status code """

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    body = response.read()
    res = """Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(body), body, body.decode("utf-8"))
    print(res)
