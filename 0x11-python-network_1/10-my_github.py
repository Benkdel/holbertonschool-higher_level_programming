#!/usr/bin/python3
"""
    Task 10
"""

if __name__ == "__main__":

    import requests
    from sys import argv

    url_api = "https://api.github.com/user"

    response = requests.get(url_api, auth=(argv[1], argv[2]))
    response = response.json()
    print(response.get("id"))
