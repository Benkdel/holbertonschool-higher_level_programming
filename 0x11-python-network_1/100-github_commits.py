#!/usr/bin/python3
"""
Task 11
"""


def api_github(path="", params=""):
    """ Request to api of github """
    import requests
    api_github = "https://api.github.com"
    url = api_github + "/" + path + params
    response = requests.get(url)
    return response


if __name__ == "__main__":
    from sys import argv

    [repo, owner] = argv[1:]

    commits = api_github("repos/{}/{}/commits?per_page=10".format(owner, repo))
    commits = commits.json()
    for commit in commits:
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")
        ))
