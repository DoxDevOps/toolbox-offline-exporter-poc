import os
import time

time.sleep(10)
os.system("cd ~ && cd /var/www/toolbox-offline-exporter-poc/ && python app.py > app.log 2>&1")

