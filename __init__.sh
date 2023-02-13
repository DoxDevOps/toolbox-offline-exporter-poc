#!/bin/bash

cd /var/www/toolbox-offline-exporter-poc/

# Activate the virtual environment
source flask/bin/activate

/usr/bin/python /var/www/toolbox-offline-exporter-poc/start.py
