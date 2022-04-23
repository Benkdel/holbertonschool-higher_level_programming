#!/usr/bin/python3
"""
task 3
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
