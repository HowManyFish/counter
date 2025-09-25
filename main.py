from box import Box
from ultrasonic_sensor import Sensor
from influx_db import Transmitter
from led_flash import led_off, led_on
import os

led_off() # NOTE: makes sure the led is off

transmitter = Transmitter(
    token = os.environ.get("INFLUXDB_TOKEN"),
    org = "fishy",
    url = "https://us-central1-1.gcp.cloud2.influxdata.com",
    bucket="FishyDataV2",
    device_name = "Pi"
)

transmitter.initalise_conection()

box = Box(
    sensors = [
        Sensor((24, 23)),
        Sensor((22, 27))
    ],
    mesurement_history_len = 12
)

box.calabrate_sensors(5)

while True:
    box.scan(transmitter)
