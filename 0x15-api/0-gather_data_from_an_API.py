#!/usr/bin/python3

"""
This script talks to jsonplaceholder api to fetch
data about a user that includes the name of the user from
"""


import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
