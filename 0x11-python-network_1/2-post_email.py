#!/usr/bin/python3
""" post request

    1. takes url and email
    2. sends post request
    3. display body decoded in utf-8
 """

if __name__ == "__main__":

    import urllib.request
    import urllib.parse
    from sys import argv

    [url, email] = argv[1:]
    params = {"email": email}
    data = urllib.parse.urlencode(params)
    data = data.encode("ascii")
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
