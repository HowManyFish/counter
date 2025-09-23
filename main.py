from Grapple_test import Container,Fish
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
box.get_water_level(1)
print("and now fish")
sleep(10)
box.add_fish(2700,1)

trans = Transmitter(token,org,url,bucket,"Pi")
trans.initalise_conection()

for fish in box.fish_in_box:
    fish.Calc_weight()
    print(fish)
    trans.send_data(fish.weight)