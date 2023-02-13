#!/bin/bash
(crontab -l 2>/dev/null; echo "@reboot /var/www/toolbox-offline-exporter-poc/__ini__.sh") | crontab -
