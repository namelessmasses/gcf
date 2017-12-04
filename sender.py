#!/usr/bin/python

import RPi.GPIO as gpio
from cloudiot_http_example import create_jwt
import requests
import json
import base64
import time

publish_url = 'https://cloudiot-device.googleapis.com/v1beta1/projects/plasma-sol-181606/registries/ngarimu-reg-0/devices/device0:publishEvent'

jwt = create_jwt('plasma-sol-181606', 'device0/rsa_private_device0.pem', 'RS256').decode('utf-8')

headers = {
    'Authorization': 'Bearer {}'.format(jwt),
    'Context-Type': 'application/json'
}

gpio.setmode(gpio.BCM)
gpio.setup(13, gpio.IN)

try:
    oldpin = gpio.input(13)
    print(oldpin)
    while True:
        payload = gpio.input(13)
        if payload != oldpin:
            oldpin = payload
            print(payload)
            body = {
                'binary_data': base64.urlsafe_b64encode('{}'.format(payload).encode('utf-8')).decode('utf-8')
            }
            print(body)
            resp = requests.post(
                publish_url,
                data = json.dumps(body),
                headers = headers)

            print(resp)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

gpio.cleanup()
