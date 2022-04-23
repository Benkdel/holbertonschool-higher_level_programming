#!/usr/bin/python3
"""
task 6
"""

if __name__ == "__main__":

    import requests
    from sys import argv

    [url, email] = argv[1:]

    send_values = {"email": email}
    response = requests.post(url, data=send_values)
    print(response.text)
