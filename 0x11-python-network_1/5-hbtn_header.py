#!/usr/bin/python3
"""
task 5
"""

if __name__ == "__main__":

    import requests
    from sys import argv

    url = argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
