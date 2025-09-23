from fish_classes import Container,Fish
from influx_db import Transmitter
from time import sleep
import os

token = os.environ.get("INFLUXDB_TOKEN")
org = "fishy"
url = "https://us-central1-1.gcp.cloud2.influxdata.com"
bucket="FishyData"

box = Container(0.55,0.40)
box.add_sensor((24,23))
box.add_sensor((21,20))
box.add_controller()
box.zero_sensor(5)

while True:
    box.get_water_level(5)
    print("and now fish")
    box.add_fish(1000,5)
    box.total_weight()

    trans = Transmitter(token,org,url,bucket,"Pi")
    trans.initalise_conection()

    for fish in box.fish_in_box:
        fish.Calc_weight()
        print(fish)
        print(box.weight)
        trans.send_data(fish.weight,box.water_level,box.weight)