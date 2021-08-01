#!/usr/bin/env python3

import requests
import datetime
import pytz
import os
from pathlib import Path

parameter_id = 'xO44xK7T'

config = {}

env_file_path = os.path.join(Path(__file__).parent.resolve(), '.env')

with open(env_file_path) as f:
    for line in f.readlines():
        config_name, config_option = line.split('=')
        config[config_name] = config_option.rstrip()


headers = {
    'Accept': 'Application/json',
    'Authorization': 'Bearer ' + config['API_KEY']
}

request = requests.get(f'https://meteo.pileus.si/api/data?parameterIds[]={config["PARAMETER_ID"]}',headers=headers)

response = request.json()

if response['dataAvailable']:
    datapoint = response['data'][0]

    # Parse string to datetime and set timezone as UTC
    datapoint['DateTime'] = datetime.datetime.strptime(datapoint['DateTime'], '%Y-%m-%d %H:%M:%S').replace(tzinfo=datetime.timezone.utc)

    local_timezone = pytz.timezone(config["LOCAL_TIMEZONE"])

    # Get current time with local timezone
    current_time = datetime.datetime.now(tz=local_timezone)


    # Make sure datapoint is less than 1 hour old
    if  current_time - datapoint['DateTime'] < datetime.timedelta(hours=1):
        print(f'{config["PARAMETER_NAME"]} @ {datapoint["DateTime"].astimezone(local_timezone).strftime("%H:%M")} {datapoint[config["PARAMETER_ID"]]}°C')
    else:
        print('')
else:
    print('')
    