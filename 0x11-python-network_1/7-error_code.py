#!/usr/bin/python3
"""
Task 7
"""
if __name__ == "__main__":

    import requests
    from sys import argv

    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
