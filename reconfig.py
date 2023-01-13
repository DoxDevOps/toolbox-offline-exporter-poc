#! /usr/bin/python
from utils.setup_other_apps import choose_app
from utils.setup_toolbox import get_facility_name
print("**************** Re-configure Site details ******************")

get_facility_name()

print("Lastly, configure other modules installed ")
choose_app()

print("**************** FINISHED RECONFIGURATION ******************")