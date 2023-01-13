"""
This file contains functions that handle serial numbers
"""


def get_host_serial():
    """
    a function that read serial stored in a file
    :return: serial as str
    """
    file = open("config/___rapt___.txt", "r")
    serial = file.read()
    file.close()
    return serial.strip()


def save_host_serial(serial):
    """
    a function that stores serial in a file
    :param serial: serial to be stored
    :return: serial as str
    """
    file = open("config/___rapt___.txt", "w")
    file.write(serial.strip())
    file.close()
    return serial.strip()
