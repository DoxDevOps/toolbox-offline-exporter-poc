# coding=utf-8

""" These are universal functions that do not depend on any other function/ functionality of toolbox"""
import json
import requests


def load_file(location):
    """
    a function that loads a json file
    :type location: string
    :return: json object
    """
    with open(location) as f:
        data = json.load(f)
    return data


def write_file(location, info):
    """
    function that writes to a json file
    :param location: where the json file is located
    :param info: info to write to json file
    :return:  boolean (just a checker)
    """
    with open(location, "w") as data:
        data.write(json.dumps(info))
        data.close()
    return True


def get_request(url, token, body):
    """
    makes a get request based on keywords sent from the body
    :param url: endpoint
    :param token: for authorization
    :param body: data to be sent to the endpoint
    :return: info from the endpoint
    """
    headers = \
        {
            'Authorization': token,
            'Content-Type': 'application/json',
            'Accept': 'text/plain',
            'Content-type': 'application/json'
        }
    results = requests.get(url, data=body, headers=headers)
    # print(results.json())
    results = json.dumps(results.json())

    return results

def get_all(url, token):
    """
    makes a get request based on keywords sent from the body
    :param url: endpoint
    :param token: for authorization
    :param body: data to be sent to the endpoint
    :return: info from the endpoint
    """
    headers = \
        {
            'Authorization': token,
            'Content-Type': 'application/json',
            'Accept': 'text/plain',
            'Content-type': 'application/json'
        }
    results = requests.get(url, headers=headers)
    return results
