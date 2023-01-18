# coding=utf-8
# !/bin/bash
import json
import re
import subprocess
import uuid

from utils.get_serial import save_host_serial
from utils.utilities import load_file, get_all, write_file
from utils.validate_emr_data import save_facility_details


def offline_setup():
    """
    This step is for offline installation on POC. It get all sites and save them in a json file
    :return:
    """

    settings = load_file("config/.json")
    url = settings["endpoint"]
    token = settings["token"]
    results = get_all(url, token)

    results = results.json()

    write_file(settings["sites_dir"], results)
    return True


def get_facility_name():
    """
    starting point. prompts user to enter a suggested facility name
    :return: Boolean (just a checker )
    """
    facility_name = raw_input("Enter Facility Name Please: ")
    search_facilities(facility_name)
    return True


def search_facilities(facility_name):
    """
    get suggested name and search in a remote server
    :param facility_name: string
    :return: boolean (just a checker)
    """
    settings = load_file("config/.json")
    data = load_file(settings["sites_dir"])
    data = json.dumps(data)

    facilities = json.loads(data)
    found_sites = []
    counter = 0
    for facility in facilities:
        if facility_name.lower() in (facility['fields']['name']).lower():
            counter += 1
            found_sites.append(facility)

    if len(found_sites) != 2:
        display_facilities(found_sites)
    else:
        print("\n No match Found, Please try again:")
        get_facility_name()

    return True


def display_facilities(facilities):
    """
    displays all possible sites
    :param facilities: json object
    :return:
    """
    facilities = json.dumps(facilities)
    facilities = json.loads(facilities)
    counter = 0
    for facility in facilities:
        counter += 1
        print(str(counter) + " " + facility['fields']['name'])
    select_facility(facilities, counter)
    return True


def select_facility(facilities, counter):
    """
    gives a user an option to select sites from a given list
    :type counter: int
    :type facilities: json object
    :param facilities: json object
    :param counter: a counter on the number of sites retrieved
    """
    while True:
        try:
            facility_number = int(raw_input("\nConfirm Facility Name by Entering a Number: ")) - 1

            if facility_number + 1 > counter:
                print("The number selected is not on the list, Please try again.")
                continue
            if facility_number < 0:
                print("Please Select a POSITIVE number")
                continue
            save_facility(facilities, facility_number)
        except ValueError:
            print("\nPlease enter a valid number")
            continue
        else:
            break


def save_facility(facilities, facility_number):
    """
    saves facility details after configuration
    :type facilities: json object
    :type facility_number: int
    :param facilities:
    :param facility_number: number se
    :return: Boolean
    """
    selected_facility = facilities[facility_number]['fields']['name']
    site_data = {"apps": facilities[facility_number]['fields']['apps'], "name": selected_facility,
                 "uuid": facilities[facility_number]['fields']['uuid']}
    print("Selected District : " + selected_facility)
    save_facility_details(site_data)  # then save the details in config file
    return True


def mac_address():
    """
    gets machine MAC address
    :return:
        mac_address : mac address of a machine
    """
    # convert to hex and separate two figures with :
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac


def get_serial():
    """
    gets machine Serial number
    :return:
        host_serial_number : serial number of a machine
    """
    # password for admin access permenisions
    # linux (debian) for geting srial numbetr
    command = 'sudo dmidecode -s system-serial-number'.split()
    cmd2 = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = cmd2.stdout.read().strip()
    save_host_serial(output.decode())
    return output
