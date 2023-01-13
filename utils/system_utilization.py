import platform
import subprocess
import json
import psutil
from psutil._common import bytes2human
import distro as distro


_ram_ = psutil.virtual_memory()
_hdd_ = psutil.disk_usage('/')


def get_cpu_utilization():
    """
    A function that checks CPU utilization
    :return: percentage of the CPU used
    """
    data = psutil.cpu_percent()
    return data


def get_ram_details():
    """
    Function that checks RAM stats on a site
    :return: Json Object that contains all RAM details
    """
    ram_dict = \
        {
            "total_ram": bytes2human(_ram_.total),
            "used_ram": bytes2human(_ram_.used),
            "remaining_ram": bytes2human(_ram_.free),
            # "percentage": int(_ram_.percent)

        }
    json_object = json.dumps(ram_dict)
    json_object = json.loads(json_object)
    return json_object


def get_hdd_details():
    """
    Function that gets HDD stats
    :return: Json Object containing HDD stats
    """
    hdd_dict = \
        {
            "hdd_total_storage": bytes2human(_hdd_.total),
            "hdd_used_storage": bytes2human(_hdd_.used),
            "hdd_remaining_storage": bytes2human(_hdd_.free),
            "hdd_used_in_percentiles": int(_hdd_.percent)
        }
    json_object = json.dumps(hdd_dict)
    json_object = json.loads(json_object)
    return json_object


def check_service():
    """
    Checks if the services are up or not
    :return:
    """
    services = ["docker", "mysql", "nginx"]  # service to check (Active or Inactive)
    running_services_dict = {}
    for service in services:
        p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')
        running_services_dict[service] = output

    json_object = json.dumps(running_services_dict)

    return json_object


def platform_info():
    """
    Check the Version of Ubuntu running at a site
    :return:
    """
    os_info = distro.os_release_info()
    return os_info
