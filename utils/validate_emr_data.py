# coding=utf-8
import json

from utils.utilities import write_file
from config.config import data, setup_emr, modules


def validate_config_file(location):
    """
    validates if data is in the correct format
    :return: Return False when the file is not correct
    """
    try:
        with open(location) as f:
            return json.load(f)
    except ValueError as e:
        return False


def save_facility_details(site_data):  # this function will be called whe we implement a POP UP MENU for Site
    """
    gets facility details as dictionary and saves the file as a json file
    :param site_data:
    :return:
    """
    # details to be entered on the web browser
    if site_data["apps"][0] == "Point of Care":
        app_id = 1
        information = {"core": setup_emr["core"], "api": setup_emr["api"]}
        write_file(data["apps_loc"], information)
    else:
        app_id = 2
        information_emc = {"emc": setup_emr["emc"]}
        write_file(data["apps_loc"], information_emc)

    site_name = site_data["name"]
    uuid = site_data["uuid"]
    information = {"uuid": uuid, "app_id": app_id, "site_name": site_name}
    write_file(data["config"], information)
    return True


def append_other_apps(app_id):
    """
    appends other 'app' data to the apps.json file
    :param app_id:
    :return:
    """
    # ("1. NONE \n 2. ANC \n 3. Maternity \n 4. HTS \n 5. OPD \n ")
    if app_id == 2:
        location = {"anc": modules["anc"]}
    if app_id == 3:
        location = {"maternity": modules["maternity"]}
    if app_id == 4:
        location = {"hts": modules["hts"]}
    if app_id == 5:
        location = {"opd": modules["opd"]}

    # Read JSON file
    with open(data["apps_loc"]) as apps:
        apps = json.load(apps)

    # appending the data
    apps.update(location)
    write_file(data["apps_loc"], apps)
    return True
