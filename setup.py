#! /usr/bin/python
import os

from utils.setup_toolbox import mac_address, get_serial, get_facility_name


def configure_site():
    """
       configures toolbox
       :return:
       """
    print("********** LET'S SET UP TOOLBOX ON THE SERVER **********")
    print("..........")
    print("Installing Requirements ...")
    # os.system(". flask/bin/activate && pip install --no-index --find-links='./packages' -r requirements.txt")

    os.system(". flask/bin/activate && python -c 'from utils.setup_toolbox import "
              "get_facility_name; "
              "get_facility_name()'")
    #mac_address()
    print("*********** END - Facility Configured Successfully *****************")
    print("creating Toolbox Service")
    #os.system("sudo cp toolbox.desktop ~/Desktop/")
    # here is the code for creating the site.
    os.system("sudo cp toolbox.service /etc/systemd/system/")
    os.system("sudo systemctl daemon-reload && sudo systemctl start toolbox && sudo systemctl enable toolbox")
    print("FINISHED :creating Toolbox Service \n")
    print("******************************************************************** \n")
    #print ("Lastly select other modules installed !")
    #os.system(". flask/bin/activate && python -c 'from utils.setup_other_apps import "
    #          "choose_app; "
    #          "choose_app()'")
    #print("FINISHED :Setting up other modules")
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
