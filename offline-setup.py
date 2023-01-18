#! /usr/bin/python
import os

from utils.setup_toolbox import mac_address, get_serial, get_facility_name


def configure_site():
    """
       configures toolbox
       :return:
       """
    # Configures the site
    # install pip
    print("********************")
    print("*** WELCOME TO TOOBOX-OFFLINE-EXPORTER FOR POINT OF CARE (POC) ***")
    print("Starting ..........")
    print("1. Update modules")
    answer = os.system("sudo apt-get update")
    print("Step 2: Install Pip.")
    os.system("sudo apt install python-pip")
    print("Step3 : install python environment")
    os.system("sudo apt install virtualenv")
    os.system("virtualenv flask")
    print("Installing requirements .....")
    os.system(". flask/bin/activate && pip install -r requirements.txt && sudo apt-get install git")

    print("******************** ABOUT TO FINISH ********************")
    os.system(". flask/bin/activate && python -c 'from utils.setup_toolbox import "
              "offline_setup; "
              "offline_setup()'")
    print("*********** END - OFFLINE SETUP COMPLETE :) !!!! *****************")

    return True


def main():
    """
    startup function
    :return: boolean
    """
    configure_site()
    return True


if __name__ == '__main__':
    main()
