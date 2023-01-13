import json
from os.path import exists

import jsonify as jsonify
from flask import Flask, render_template
from config.config import data
from utils.export_emr_data import check_installation_folders
from utils.generate_qr_image import add_qr_data
from utils.get_serial import get_host_serial
from utils.setup_toolbox import mac_address, get_serial
from utils.system_utilization import get_hdd_details, get_ram_details, platform_info, get_cpu_utilization
from utils.utilities import load_file
from utils.validate_emr_data import validate_config_file


app = Flask(__name__, static_folder="templates/static")


@app.route('/test')
def test():

    return jsonify({"SUCCESS": "System is perfectly working"})


@app.route('/')
def extract_data():
    """gets EMR data and creates a QR Image
    Args: None
    Returns:
        dict: hosts from api
    """
    # check if the serial key has been retrieved
    if not exists(data["serial_key"]):
        get_serial() # if the serial key is not available, then create one

    # first verify if the data is correct in the config file

    config_file_data = validate_config_file(data["config"])
    apps_file_data = validate_config_file(data["apps_loc"])
    if not config_file_data or not apps_file_data:
        return render_template('error.html')  # this will load a page that informs the user to reconfigure toolbox
    # if all is alright, then do the following
    # 1. get EMR version and mac address
    emr_data = check_installation_folders(data["apps_loc"])
    mac = mac_address()
    # 2. Get Serial number
    serial_number = get_host_serial()
    # 3. get System Utilization Stats and OS details
    hdd = get_hdd_details()
    ram = get_ram_details()
    os_info = platform_info()
    cpu = get_cpu_utilization()

    if not emr_data:
        return render_template('error.html')
    # 2. This is a final Dictionary to be sent for QR Image generation
    final_emr_data = \
        {
            "1": "Toolbox",
            "uuid": config_file_data["uuid"],
            "app_id": config_file_data["app_id"],
            "system_utilization": {
                "hdd_total_storage": hdd["hdd_total_storage"],
                "hdd_used_storage": hdd["hdd_used_storage"],
                "hdd_remaining_storage": hdd["hdd_remaining_storage"],
                "hdd_used_in_percentiles": hdd["hdd_used_in_percentiles"],
                "total_ram": ram["total_ram"],
                "used_ram": ram["used_ram"],
                "remaining_ram": ram["remaining_ram"],
                "cpu_utilization": cpu,
                "os_name": os_info["name"],
                "os_version": os_info["version"]},
            "module": emr_data,
            "serial_number": serial_number

        }

    final_string_to_decrypt = json.dumps(final_emr_data)
    # 3. Add the data to QR Image
    add_qr_data(final_string_to_decrypt, data["toolbox_image"])

    # 4 Get facility name . This name will be displayed on UI
    site_name = load_file(data["config"])
    return render_template('index.html', site_name=site_name["site_name"])


@app.route('/getImage', methods=['GET'])
def get_image_url():
    """
    Api endpoint that gets the qr image url and site name
    :return: json
    """
    image_url = data["toolbox_image"]
    site_name = load_file(data["config"])
    return jsonify({'url': image_url, 'site': site_name["site_name"]})


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=6070)
